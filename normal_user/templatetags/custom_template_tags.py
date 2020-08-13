from django import template
import json
from normal_user.models import *
from django.contrib.auth.models import User
from datetime import datetime,date, timedelta
import pytz
from dateparser import parse
register = template.Library()


@register.simple_tag
def last_hba1c(user_id):
	user_details = UserDetails.objects.filter(manager_id = int(user_id)).order_by("-id")[0:5]
	return user_details


@register.simple_tag
def userComment(user_id):
	try:
		user_comment = CommentsModel.objects.get(staff_user_id_id = int(user_id))
		return user_comment
	except:
		return ""

@register.simple_tag
def user_status(user_id):
	try:
		user_status_obj = OnlineStatusModel.objects.get(user_id = int(user_id))

		if user_status_obj.i_am_here:
			user_status_ = "Online"
			icon_class = "green"
		elif user_status_obj.in_meeting:
			user_status_ = "In Meeting"
			icon_class = "orange"
		elif user_status_obj.lunch_break:
			user_status_ = "Lunch Break"
			icon_class = "orange"
		elif user_status_obj.tea_break:
			user_status_ = "Tea Break"
			icon_class = "orange"
		else:
			user_status_ = "Offline"
			icon_class = "red"
		context = {}
		context["user_status"] = user_status_
		context["icon_class"] = icon_class
		return context
	except:
		return ""


@register.simple_tag
def user_name(user_email):
	try:
		user_name = UserDetails.objects.get(user__username = user_email)
		return user_name.name
	except:
		return ""

@register.simple_tag
def user_schedules(user__id):
	try:
		user_obj = UserDetails.objects.get(user_id = user__id)
		user_time = pytz.timezone(user_obj.timezone)
		user_time_ = datetime.now(user_time)
		# user_time = user_time_.strftime('%Y-%m-%d %I:%M:%S')
		user_obj = ScheduleTiming.objects.filter(user_id = user__id,  start_date__gte = user_time_)
		return user_obj
	except Exception as k:
		print("---------------",k)
		return ""


@register.simple_tag
def time_difference(start_date,time_1, time2):
	try:
		start_date = parse(str(start_date)+" , "+ str(time_1))
		if start_date.date() == time2.date():
			# user_time_ = parse(user_time_.strftime('%Y-%m-%d %I:%M:%S'))
			user_time_hour = (start_date.hour) + (start_date.minute/60)
			last_time_hour = (time2.hour) + (time2.minute/60)
			final_minutes = abs(user_time_hour - last_time_hour)
		else:
			time_fifference = start_date - time2
			time_fifference = time_fifference.hour + (time_fifference.minute/60)
			final_minutes = abs(time_fifference)

		time = str(timedelta(minutes= (final_minutes * 60)))
		split_time = time.split(":")
		split_time = split_time[0]+":"+split_time[1]
		return split_time
	except:
		return ""


@register.simple_tag
def task_split(task):
	try:
		task = Tasks.objects.filter(task_id_id = int(task))
		return task
	except:
		return ""


@register.simple_tag
def chat_info(thread_id, user_id):
	try:
		context = {}
		chat_obj = ChatMessage.objects.filter(thread_id = thread_id).last()

		if chat_obj:
			context["last_message"] = chat_obj.message
			context["time"] = chat_obj.created
			if user_id == chat_obj.sender.id:
				reciever_id = chat_obj.reciever.id
			else:
				reciever_id = chat_obj.sender.id
		else:
			thread_obj = ChatThread.objects.get(id = int(thread_id))
			context["last_message"] = ""
			context["time"] = ""
			if user_id == thread_obj.sender.id:
				reciever_id = thread_obj.reciever.id
			else:
				reciever_id = thread_obj.sender.id
		try:
			reciever_name_s = UserDetails.objects.get(user_id = reciever_id)
			reciever_name = reciever_name_s.name
			reciever_id = reciever_name_s.user.id
			reciever_email = reciever_name_s.user.username
			reciever_email_id = reciever_email.replace(".", "")
			reciever_email_id = reciever_email_id.replace("@", "")
		except:
			try:
				reciever_name_s = ManagerDetails.objects.get(manaager_id = reciever_id)
				reciever_name = reciever_name_s.full_name
				reciever_id = reciever_name_s.manaager.id
				reciever_email = reciever_name_s.manaager.username
				reciever_email_id = reciever_email.replace(".", "")
				reciever_email_id = reciever_email_id.replace("@", "")
			except:
				reciever_id = ""
				reciever_email_id = ""
				reciever_name = ""
				reciever_email = ""
		context["reciever_name"] = reciever_name
		context["reciever_email"] = reciever_email
		context["reciever_email_id"] = reciever_email_id
		context["reciever_id"] = reciever_id


		return context
	except Exception as j:
		print(j)
		return ""


@register.simple_tag
def email_reply_split(email_reply):
	try:
		if ":====:" in email_reply:
			email_reply_split = email_reply.split(":====:")
			email_reply_html = ""
			for i in email_reply_split:
				email_reply_html += i+"</br>"
			return email_reply_html
		else:
			return email_reply
	except:
		return ""


@register.simple_tag
def manager_chat_info(thread_id, user_id):
	try:
		context = {}
		chat_obj = ChatMessage.objects.filter(thread_id = thread_id).last()
		
		context["last_message"] = chat_obj.message
		context["time"] = chat_obj.created

		try:
			reciever_name_s = UserDetails.objects.get(user_id = chat_obj.reciever.id)
			reciever_name = reciever_name_s.name
		except:
			reciever_name_s = ManagerDetails.objects.get(manaager_id = chat_obj.reciever.id)
			reciever_name = reciever_name_s.full_name
		context["reciever_name"] = reciever_name


		try:
			sender_name_s = UserDetails.objects.get(user_id = chat_obj.sender.id)
			sender_name = sender_name_s.name
			context["sender_id"] = sender_name_s.user.id
		except:
			sender_name_s = ManagerDetails.objects.get(manaager_id = chat_obj.sender.id)
			sender_name = sender_name_s.full_name
			context["sender_id"] = sender_name_s.manaager.id
		context["sender_name"] = sender_name
		# if user_id == chat_obj.sender.id:
		# 	reciever_id = chat_obj.reciever.id
		# else:
		# 	reciever_id = chat_obj.sender.id

		# try:
		# 	reciever_name_s = UserDetails.objects.get(user_id = reciever_id)
		# 	reciever_name = reciever_name_s.name
		# 	reciever_id = reciever_name_s.user.id
		# 	reciever_email = reciever_name_s.user.username
		# 	reciever_email_id = reciever_email.replace(".", "")
		# 	reciever_email_id = reciever_email_id.replace("@", "")
		# except:
		# 	try:
		# 		reciever_name_s = ManagerDetails.objects.get(manaager_id = reciever_id)
		# 		reciever_name = reciever_name_s.full_name
		# 		reciever_id = reciever_name_s.manaager.id
		# 		reciever_email = reciever_name_s.manaager.username
		# 		reciever_email_id = reciever_email.replace(".", "")
		# 		reciever_email_id = reciever_email_id.replace("@", "")
		# 	except:
		# 		reciever_id = ""
		# 		reciever_email_id = ""
		# 		reciever_name = ""
		# 		reciever_email = ""
		# context["reciever_name"] = reciever_name
		# context["reciever_email"] = reciever_email
		# context["reciever_email_id"] = reciever_email_id
		# context["reciever_id"] = reciever_id
		return context
	except:
		return ""
