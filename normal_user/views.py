from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.views import View
from datetime import datetime, timedelta
from django.core.files.storage import default_storage
import os, json
from django.conf import settings
from django.utils.decorators import method_decorator
from .decorators import *
from websocket import create_connection
from django.core.paginator import Paginator
from time import sleep
import pytz
from dateparser import parse
import asyncio
from django.db.models.functions import (
    ExtractDay, ExtractHour, ExtractMinute, ExtractMonth,
    ExtractQuarter, ExtractSecond, ExtractWeek, ExtractWeekDay,
    ExtractYear,
)
from django.db.models import Q
import time
from django.template import loader
import base64

socket_url = settings.SOCKET_URL


all_timezones = ["Africa/Abidjan","Africa/Accra","Africa/Addis_Ababa","Africa/Algiers","Africa/Asmara","Africa/Asmera","Africa/Bamako","Africa/Bangui","Africa/Banjul","Africa/Bissau","Africa/Blantyre","Africa/Brazzaville","Africa/Bujumbura","Africa/Cairo","Africa/Casablanca","Africa/Ceuta","Africa/Conakry","Africa/Dakar","Africa/Dar_es_Salaam","Africa/Djibouti","Africa/Douala","Africa/El_Aaiun","Africa/Freetown","Africa/Gaborone","Africa/Harare","Africa/Johannesburg","Africa/Juba","Africa/Kampala","Africa/Khartoum","Africa/Kigali","Africa/Kinshasa","Africa/Lagos","Africa/Libreville","Africa/Lome","Africa/Luanda","Africa/Lubumbashi","Africa/Lusaka","Africa/Malabo","Africa/Maputo","Africa/Maseru","Africa/Mbabane","Africa/Mogadishu","Africa/Monrovia","Africa/Nairobi","Africa/Ndjamena","Africa/Niamey","Africa/Nouakchott","Africa/Ouagadougou","Africa/Porto-Novo","Africa/Sao_Tome","Africa/Timbuktu","Africa/Tripoli","Africa/Tunis","Africa/Windhoek","America/Adak","America/Anchorage","America/Anguilla","America/Antigua","America/Araguaina","America/Argentina/Buenos_Aires","America/Argentina/Catamarca","America/Argentina/ComodRivadavia","America/Argentina/Cordoba","America/Argentina/Jujuy","America/Argentina/La_Rioja","America/Argentina/Mendoza","America/Argentina/Rio_Gallegos","America/Argentina/Salta","America/Argentina/San_Juan","America/Argentina/San_Luis","America/Argentina/Tucuman","America/Argentina/Ushuaia","America/Aruba","America/Asuncion","America/Atikokan","America/Atka","America/Bahia","America/Bahia_Banderas","America/Barbados","America/Belem","America/Belize","America/Blanc-Sablon","America/Boa_Vista","America/Bogota","America/Boise","America/Buenos_Aires","America/Cambridge_Bay","America/Campo_Grande","America/Cancun","America/Caracas","America/Catamarca","America/Cayenne","America/Cayman","America/Chicago","America/Chihuahua","America/Coral_Harbour","America/Cordoba","America/Costa_Rica","America/Creston","America/Cuiaba","America/Curacao","America/Danmarkshavn","America/Dawson","America/Dawson_Creek","America/Denver","America/Detroit","America/Dominica","America/Edmonton","America/Eirunepe","America/El_Salvador","America/Ensenada","America/Fort_Nelson","America/Fort_Wayne","America/Fortaleza","America/Glace_Bay","America/Godthab","America/Goose_Bay","America/Grand_Turk","America/Grenada","America/Guadeloupe","America/Guatemala","America/Guayaquil","America/Guyana","America/Halifax","America/Havana","America/Hermosillo","America/Indiana/Indianapolis","America/Indiana/Knox","America/Indiana/Marengo","America/Indiana/Petersburg","America/Indiana/Tell_City","America/Indiana/Vevay","America/Indiana/Vincennes","America/Indiana/Winamac","America/Indianapolis","America/Inuvik","America/Iqaluit","America/Jamaica","America/Jujuy","America/Juneau","America/Kentucky/Louisville","America/Kentucky/Monticello","America/Knox_IN","America/Kralendijk","America/La_Paz","America/Lima","America/Los_Angeles","America/Louisville","America/Lower_Princes","America/Maceio","America/Managua","America/Manaus","America/Marigot","America/Martinique","America/Matamoros","America/Mazatlan","America/Mendoza","America/Menominee","America/Merida","America/Metlakatla","America/Mexico_City","America/Miquelon","America/Moncton","America/Monterrey","America/Montevideo","America/Montreal","America/Montserrat","America/Nassau","America/New_York","America/Nipigon","America/Nome","America/Noronha","America/North_Dakota/Beulah","America/North_Dakota/Center","America/North_Dakota/New_Salem","America/Ojinaga","America/Panama","America/Pangnirtung","America/Paramaribo","America/Phoenix","America/Port-au-Prince","America/Port_of_Spain","America/Porto_Acre","America/Porto_Velho","America/Puerto_Rico","America/Punta_Arenas","America/Rainy_River","America/Rankin_Inlet","America/Recife","America/Regina","America/Resolute","America/Rio_Branco","America/Rosario","America/Santa_Isabel","America/Santarem","America/Santiago","America/Santo_Domingo","America/Sao_Paulo","America/Scoresbysund","America/Shiprock","America/Sitka","America/St_Barthelemy","America/St_Johns","America/St_Kitts","America/St_Lucia","America/St_Thomas","America/St_Vincent","America/Swift_Current","America/Tegucigalpa","America/Thule","America/Thunder_Bay","America/Tijuana","America/Toronto","America/Tortola","America/Vancouver","America/Virgin","America/Whitehorse","America/Winnipeg","America/Yakutat","America/Yellowknife","Antarctica/Casey","Antarctica/Davis","Antarctica/DumontDUrville","Antarctica/Macquarie","Antarctica/Mawson","Antarctica/McMurdo","Antarctica/Palmer","Antarctica/Rothera","Antarctica/South_Pole","Antarctica/Syowa","Antarctica/Troll","Antarctica/Vostok","Arctic/Longyearbyen","Asia/Aden","Asia/Almaty","Asia/Amman","Asia/Anadyr","Asia/Aqtau","Asia/Aqtobe","Asia/Ashgabat","Asia/Ashkhabad","Asia/Atyrau","Asia/Baghdad","Asia/Bahrain","Asia/Baku","Asia/Bangkok","Asia/Barnaul","Asia/Beirut","Asia/Bishkek","Asia/Brunei","Asia/Calcutta","Asia/Chita","Asia/Choibalsan","Asia/Chongqing","Asia/Chungking","Asia/Colombo","Asia/Dacca","Asia/Damascus","Asia/Dhaka","Asia/Dili","Asia/Dubai","Asia/Dushanbe","Asia/Famagusta","Asia/Gaza","Asia/Harbin","Asia/Hebron","Asia/Ho_Chi_Minh","Asia/Hong_Kong","Asia/Hovd","Asia/Irkutsk","Asia/Istanbul","Asia/Jakarta","Asia/Jayapura","Asia/Jerusalem","Asia/Kabul","Asia/Kamchatka","Asia/Karachi","Asia/Kashgar","Asia/Kathmandu","Asia/Katmandu","Asia/Khandyga","Asia/Kolkata","Asia/Krasnoyarsk","Asia/Kuala_Lumpur","Asia/Kuching","Asia/Kuwait","Asia/Macao","Asia/Macau","Asia/Magadan","Asia/Makassar","Asia/Manila","Asia/Muscat","Asia/Nicosia","Asia/Novokuznetsk","Asia/Novosibirsk","Asia/Omsk","Asia/Oral","Asia/Phnom_Penh","Asia/Pontianak","Asia/Pyongyang","Asia/Qatar","Asia/Qostanay","Asia/Qyzylorda","Asia/Rangoon","Asia/Riyadh","Asia/Saigon","Asia/Sakhalin","Asia/Samarkand","Asia/Seoul","Asia/Shanghai","Asia/Singapore","Asia/Srednekolymsk","Asia/Taipei","Asia/Tashkent","Asia/Tbilisi","Asia/Tehran","Asia/Tel_Aviv","Asia/Thimbu","Asia/Thimphu","Asia/Tokyo","Asia/Tomsk","Asia/Ujung_Pandang","Asia/Ulaanbaatar","Asia/Ulan_Bator","Asia/Urumqi","Asia/Ust-Nera","Asia/Vientiane","Asia/Vladivostok","Asia/Yakutsk","Asia/Yangon","Asia/Yekaterinburg","Asia/Yerevan","Atlantic/Azores","Atlantic/Bermuda","Atlantic/Canary","Atlantic/Cape_Verde","Atlantic/Faeroe","Atlantic/Faroe","Atlantic/Jan_Mayen","Atlantic/Madeira","Atlantic/Reykjavik","Atlantic/South_Georgia","Atlantic/St_Helena","Atlantic/Stanley","Australia/ACT","Australia/Adelaide","Australia/Brisbane","Australia/Broken_Hill","Australia/Canberra","Australia/Currie","Australia/Darwin","Australia/Eucla","Australia/Hobart","Australia/LHI","Australia/Lindeman","Australia/Lord_Howe","Australia/Melbourne","Australia/NSW","Australia/North","Australia/Perth","Australia/Queensland","Australia/South","Australia/Sydney","Australia/Tasmania","Australia/Victoria","Australia/West","Australia/Yancowinna","Brazil/Acre","Brazil/DeNoronha","Brazil/East","Brazil/West","CET","CST6CDT","Canada/Atlantic","Canada/Central","Canada/Eastern","Canada/Mountain","Canada/Newfoundland","Canada/Pacific","Canada/Saskatchewan","Canada/Yukon","Chile/Continental","Chile/EasterIsland","Cuba","EET","EST","EST5EDT","Egypt","Eire","Etc/GMT","Etc/GMT+0","Etc/GMT+1","Etc/GMT+10","Etc/GMT+11","Etc/GMT+12","Etc/GMT+2","Etc/GMT+3","Etc/GMT+4","Etc/GMT+5","Etc/GMT+6","Etc/GMT+7","Etc/GMT+8","Etc/GMT+9","Etc/GMT-0","Etc/GMT-1","Etc/GMT-10","Etc/GMT-11","Etc/GMT-12","Etc/GMT-13","Etc/GMT-14","Etc/GMT-2","Etc/GMT-3","Etc/GMT-4","Etc/GMT-5","Etc/GMT-6","Etc/GMT-7","Etc/GMT-8","Etc/GMT-9","Etc/GMT0","Etc/Greenwich","Etc/UCT","Etc/UTC","Etc/Universal","Etc/Zulu","Europe/Amsterdam","Europe/Andorra","Europe/Astrakhan","Europe/Athens","Europe/Belfast","Europe/Belgrade","Europe/Berlin","Europe/Bratislava","Europe/Brussels","Europe/Bucharest","Europe/Budapest","Europe/Busingen","Europe/Chisinau","Europe/Copenhagen","Europe/Dublin","Europe/Gibraltar","Europe/Guernsey","Europe/Helsinki","Europe/Isle_of_Man","Europe/Istanbul","Europe/Jersey","Europe/Kaliningrad","Europe/Kiev","Europe/Kirov","Europe/Lisbon","Europe/Ljubljana","Europe/London","Europe/Luxembourg","Europe/Madrid","Europe/Malta","Europe/Mariehamn","Europe/Minsk","Europe/Monaco","Europe/Moscow","Europe/Nicosia","Europe/Oslo","Europe/Paris","Europe/Podgorica","Europe/Prague","Europe/Riga","Europe/Rome","Europe/Samara","Europe/San_Marino","Europe/Sarajevo","Europe/Saratov","Europe/Simferopol","Europe/Skopje","Europe/Sofia","Europe/Stockholm","Europe/Tallinn","Europe/Tirane","Europe/Tiraspol","Europe/Ulyanovsk","Europe/Uzhgorod","Europe/Vaduz","Europe/Vatican","Europe/Vienna","Europe/Vilnius","Europe/Volgograd","Europe/Warsaw","Europe/Zagreb","Europe/Zaporozhye","Europe/Zurich","GB","GB-Eire","GMT","GMT+0","GMT-0","GMT0","Greenwich","HST","Hongkong","Iceland","Indian/Antananarivo","Indian/Chagos","Indian/Christmas","Indian/Cocos","Indian/Comoro","Indian/Kerguelen","Indian/Mahe","Indian/Maldives","Indian/Mauritius","Indian/Mayotte","Indian/Reunion","Iran","Israel","Jamaica","Japan","Kwajalein","Libya","MET","MST","MST7MDT","Mexico/BajaNorte","Mexico/BajaSur","Mexico/General","NZ","NZ-CHAT","Navajo","PRC","PST8PDT","Pacific/Apia","Pacific/Auckland","Pacific/Bougainville","Pacific/Chatham","Pacific/Chuuk","Pacific/Easter","Pacific/Efate","Pacific/Enderbury","Pacific/Fakaofo","Pacific/Fiji","Pacific/Funafuti","Pacific/Galapagos","Pacific/Gambier","Pacific/Guadalcanal","Pacific/Guam","Pacific/Honolulu","Pacific/Johnston","Pacific/Kiritimati","Pacific/Kosrae","Pacific/Kwajalein","Pacific/Majuro","Pacific/Marquesas","Pacific/Midway","Pacific/Nauru","Pacific/Niue","Pacific/Norfolk","Pacific/Noumea","Pacific/Pago_Pago","Pacific/Palau","Pacific/Pitcairn","Pacific/Pohnpei","Pacific/Ponape","Pacific/Port_Moresby","Pacific/Rarotonga","Pacific/Saipan","Pacific/Samoa","Pacific/Tahiti","Pacific/Tarawa","Pacific/Tongatapu","Pacific/Truk","Pacific/Wake","Pacific/Wallis","Pacific/Yap","Poland","Portugal","ROC","ROK","Singapore","Turkey","UCT","US/Alaska","US/Aleutian","US/Arizona","US/Central","US/East-Indiana","US/Eastern","US/Hawaii","US/Indiana-Starke","US/Michigan","US/Mountain","US/Pacific","US/Pacific-New","US/Samoa","UTC","Universal","W-SU","WET","Zulu"]

class Login(TemplateView):
	""" Login View """
	template_name = ('login.html')

	def get_context_data(self, *args, **kwargs):
		# context = super(Login, self).get_context_data(*args, **kwargs)
		context = {}
		context["form"] = LoginForm()
		context["manager_form"] = AuthenticationForm()
		return context

	def post(self,request):
		context = {}
		captcha_form = request.POST.get("captcha_form")
		form = LoginForm(data=request.POST)

		if form.is_valid():
			user = User.objects.get(username=request.POST['username'])
			staff_obj = UserType.objects.filter(user_id = user.id, normal_user = True)
			manager_obj = UserType.objects.filter(user_id = user.id, manager = True)
			if staff_obj and user and user.is_superuser == False:
				invalid_attempts = InvalidAttempts.objects.get(user_id = user.id)
				if invalid_attempts.blocked == True:
					return HttpResponseRedirect(reverse('account_blocked_page'))
				else:
					user_obj = UserDetails.objects.get(user_id = user.id)
					user_time = pytz.timezone(user_obj.timezone)
					user_time_ = datetime.now(user_time)
					user_date = user_time_.strftime('%Y-%m-%d')
					user_time = user_time_.strftime('%Y-%m-%d %H:%M:%S')

					schedule_obj = ScheduleTiming.objects.filter(user_id = user.id, start_date__year = user_time_.year,  start_date__month  = user_time_.month,  start_date__day  = user_time_.day)
					if not schedule_obj:
						context['form'] = form
						context["user_details"] = {"email": request.POST['username'], "password" :request.POST['password']}
						context['no_authority'] = "You are not authorized to start the day at the moment"
						return render(request=request,template_name = self.template_name,context=context)
					else:
						if schedule_obj[0].logout_time:
							context['form'] = form
							context["user_details"] = {"email": request.POST['username'], "password" :request.POST['password']}
							context['no_authority'] = "Your shift for the day has already ended"
							return render(request=request,template_name = self.template_name,context=context)
						if str(user_time_.date()) == str(schedule_obj[0].start_date):
							user_time_ = parse(user_time_.strftime('%Y-%m-%d %H:%M:%S'))
							user_time_minutes = (user_time_.hour * 60) + user_time_.minute
							schedule_obj_minutes = (schedule_obj[0].start_time.hour * 60) + schedule_obj[0].start_time.minute
							diff = schedule_obj_minutes - user_time_minutes
							print(diff)
							if diff > 15:
								context['form'] = form
								context["user_details"] = {"email": request.POST['username'], "password" :request.POST['password']}
								context['no_authority'] = "You are not authorized to start the day at the moment"
								return render(request=request,template_name = self.template_name,context=context)
							else:
								# pass
								schedule_obj.update(login_time = user_time_)
								online_status = OnlineStatusModel.objects.get(user_id = user.id)
								online_status.i_am_here = True
								online_status.in_meeting = False
								online_status.lunch_break = False
								online_status.tea_break = False
								online_status.offline = False
								online_status.save()
								
								status = "i_am_here"

								manager_id_obj = UserDetails.objects.get(user_id = user.id)
								manager_obj = User.objects.get(id = manager_id_obj.manager_id)
								url = socket_url + "/manager_notify/"+str(manager_obj.username)+"/"
								ws = create_connection(url)

								ws.send(json.dumps({'user_id': int(manager_obj.id), "status" : status, "staff_id" : online_status.user.id}))


								status_ws = create_connection(socket_url+"/chat_bxx/")
								staff_div_id = online_status.user.username
								staff_div_id = staff_div_id.replace(".", "")
								staff_div_id = staff_div_id.replace("@", "")
								status_ws.send(json.dumps({"status" : status, "staff_div_id" : staff_div_id}))

								sleep(5)
								ws.close()
								status_ws.close()

								invalid_attempts.attempts = 0
								invalid_attempts.blocked = False
								invalid_attempts.start_time = None
								invalid_attempts.save()
								login(request, user)
								return HttpResponseRedirect(reverse('landing_page'))

						else:
							context['form'] = form
							context["user_details"] = {"email": request.POST['username'], "password" :request.POST['password']}
							context['no_authority'] = "You are not authorized to start the day at the moment"
							return render(request=request,template_name = self.template_name,context=context)
						

			elif manager_obj and user and user.is_superuser == False:
				invalid_attempts = InvalidAttempts.objects.get(user_id = user.id)
				
				if invalid_attempts.blocked == True:
					return HttpResponseRedirect(reverse('account_blocked_page'))
				else:
					user_obj = ManagerDetails.objects.get(manaager_id = user.id)
					user_time = pytz.timezone(user_obj.timezone)
					user_time_ = datetime.now(user_time)
					user_time = user_time_.strftime('%Y-%m-%d %H:%M:%S')
					online_status = OnlineStatusModel.objects.get(user_id = user.id)
					online_status.i_am_here = True
					online_status.in_meeting = False
					online_status.lunch_break = False
					online_status.tea_break = False
					online_status.offline = False
					online_status.time = user_time
					online_status.save()
					
					status = "i_am_here"
					
					status_ws = create_connection(socket_url+"/chat_bxx/")
					staff_div_id = online_status.user.username
					staff_div_id = staff_div_id.replace(".", "")
					staff_div_id = staff_div_id.replace("@", "")
					status_ws.send(json.dumps({"status" : status, "staff_div_id" : staff_div_id}))
					sleep(4)
					status_ws.close()

					invalid_attempts.attempts = 0
					invalid_attempts.blocked = False
					invalid_attempts.start_time = None
					invalid_attempts.save()
					login(request, user)
					return HttpResponseRedirect(reverse('manager_dashboard'))

			elif user.is_superuser:
				invalid_attempts = InvalidAttempts.objects.get(user_id = user.id)
				
				if invalid_attempts.blocked == True:
					return HttpResponseRedirect(reverse('account_blocked_page'))
				else:
					invalid_attempts.attempts = 0
					invalid_attempts.blocked = False
					invalid_attempts.start_time = None
					invalid_attempts.save()
					login(request, user)
					return HttpResponseRedirect(reverse('admin_dashboard'))	

		else:
			try:
				user = User.objects.get(username=request.POST['username'])
				invalid_attempts = InvalidAttempts.objects.get(user_id = user.id)
				invalid_attempts_count = invalid_attempts.attempts

				current_time = timezone.now()

				if invalid_attempts.blocked:
					return HttpResponseRedirect(reverse('account_blocked_page'))
				elif not invalid_attempts_count or invalid_attempts_count < 3 :
					invalid_attempts.attempts = invalid_attempts_count + 1
					invalid_attempts.save()
					invalid_attempts = InvalidAttempts.objects.get(user_id = user.id)
					if invalid_attempts.attempts == 1:
						invalid_attempts.start_time = current_time
						invalid_attempts.save()
					elif invalid_attempts.attempts >= 3:
						difference = current_time - invalid_attempts.start_time
						if difference.total_seconds() < 600:
							invalid_attempts.blocked = True
							invalid_attempts.save()
							return HttpResponseRedirect(reverse('account_blocked_page'))
						else:
							pass
				elif invalid_attempts_count >= 3:
					difference = current_time - invalid_attempts.start_time
					if difference.total_seconds() < 600:

						invalid_attempts.blocked = True
						invalid_attempts.save()
						return HttpResponseRedirect(reverse('account_blocked_page'))
					else:
						pass
			except:
				pass			
		context['form'] = form
		context["user_details"] = {"email": request.POST['username'], "password" :request.POST['password']}
		return render(request=request,template_name = self.template_name,context=context)


def logout_user(request):
	redirect_link = '/login'
	if request.user.is_authenticated:
		time = timezone.now()
		user_id = request.user.id
		try:
			user_obj = UserType.objects.get(user_id = user_id)
			if user_obj.normal_user:

				online_status = OnlineStatusModel.objects.get(user_id = user_id)
				online_status.i_am_here = False
				online_status.in_meeting = False
				online_status.lunch_break = False
				online_status.tea_break = False
				online_status.offline = True
				online_status.save()
				
				status = "offline"

				manager_id_obj = UserDetails.objects.get(user_id = user_id)
				manager_obj = User.objects.get(id = manager_id_obj.manager_id)
				url = socket_url +"/manager_notify/"+str(manager_obj.username)+"/"
				ws = create_connection(url)

				ws.send(json.dumps({'user_id': int(manager_obj.id), "status" : status, "staff_id" : online_status.user.id}))

				
				status_ws = create_connection(socket_url+"/chat_bxx/")
				staff_div_id = online_status.user.username
				staff_div_id = staff_div_id.replace(".", "")
				staff_div_id = staff_div_id.replace("@", "")
				status_ws.send(json.dumps({"status" : status, "staff_div_id" : staff_div_id}))

				sleep(5)
				ws.close()
				status_ws.close()
			if user_obj.manager:
				online_status = OnlineStatusModel.objects.get(user_id = user_obj.user.id)
				online_status.i_am_here = False
				online_status.in_meeting = False
				online_status.lunch_break = False
				online_status.tea_break = False
				online_status.offline = True
				online_status.save()
				
				status = "offline"

				status_ws = create_connection(socket_url+"/chat_bxx/")
				staff_div_id = online_status.user.username
				staff_div_id = staff_div_id.replace(".", "")
				staff_div_id = staff_div_id.replace("@", "")
				status_ws.send(json.dumps({"status" : status, "staff_div_id" : staff_div_id}))
				sleep(4)
				status_ws.close()
		except:
			pass
	logout(request)
	return redirect(redirect_link)


class AccountBlocked(TemplateView):
	template_name = ('account_bloked.html')


class NoPermission(TemplateView):
	template_name = "no_permission.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		if self.request.user.is_authenticated:
			if self.request.user.is_superuser:
				context["button"] = 'admin'
			else:
				user_id = self.request.user.id
				try:
					usr_obj = UserType.objects.get(user_id = user_id)
					if usr_obj.manager:
						context["button"] = 'manager'
					elif usr_obj.normal_user:
						context["button"] = 'normal_user'
				except:
					context["button"] = 'no_login'		
		else:
			context["button"] = 'no_login'

		print(context)
		return context








# Staff Employee Section
@method_decorator(checkloginEmployee, name='dispatch')
class LandingPage(TemplateView):
	""" Landing page View """
	template_name = ('staff_chat.html')

	def get_context_data(self, *args, **kwargs):
		context = {}
		context["reciever_email"] = self.request.user.username
		context["chat_obj"] = ChatMessage.objects.filter(sender_id = self.request.user.id)
	

		chat_thread = ChatThread.objects.filter(sender_id = self.request.user.id, archive = False, date_updated__isnull = False)
		chat_thread_1 = ChatThread.objects.filter(reciever_id = self.request.user.id, archive_2 = False, date_updated__isnull = False)
		context["chat_thread"] = (chat_thread | chat_thread_1).order_by('-date_updated')
		context["userdetails"] = UserDetails.objects.get(user_id = self.request.user.id)

		return context


# @method_decorator(checkloginEmployee, name='dispatch')
class StaffChatByUser(TemplateView):

	def post(self, request):
		context = {}

		thread_id = request.POST.get("data_thread")
		thread_obj = ChatThread.objects.get(id = int(thread_id))

		manager_id = request.user.id

		context['request_id'] = manager_id
		if manager_id == thread_obj.sender.id:
			reciever_email = thread_obj.reciever.username
		else:
			reciever_email = thread_obj.sender.username


		ChatThread.objects.filter(sender_id = manager_id,reciever__username = reciever_email).update(archive = False)
		ChatThread.objects.filter(reciever__username = reciever_email,sender_id = manager_id).update(archive_2 = False)



		try:
			UserType.objects.get(user__username = reciever_email)
			context["reciever_email"] = reciever_email
			reciever_div_id = reciever_email.replace(".","")
			context["reciever_div_id"] = reciever_div_id.replace("@","")
			user_div_id = (self.request.user.username).replace(".","")
			context["user_div_id"] = user_div_id.replace("@","")
			get_reciever_id = User.objects.get(username = reciever_email)
			context["reciever_id"] = get_reciever_id.id

			# sender_obj = ChatMessage.objects.filter(sender_id = self.request.user.id, reciever__username = reciever_email, thread__archive = False)
			# reciever_obj = ChatMessage.objects.filter(sender__username = reciever_email, reciever_id = self.request.user.id, thread__archive_2 = False)
			# chat_messages = (reciever_obj | sender_obj).order_by('created')

			chat_messages = ChatMessage.objects.filter(thread_id = int(thread_id), thread__archive_2 = False, thread__archive = False)

			context["thread_id"] = thread_id



			# if chat_messages:
			# 	context["thread_id"] = chat_messages[0].thread_id
			# else:
			# 	cht_thread = ChatThread.objects.filter(sender_id = manager_id, reciever_id = get_reciever_id.id)
			# 	cht_thread_1 = ChatThread.objects.filter(sender_id = get_reciever_id.id, reciever_id = manager_id)
			# 	if cht_thread:
			# 		thead_obj = ChatThread.objects.filter(sender_id = manager_id, reciever_id = get_reciever_id.id)
			# 		thread_id = cht_thread[0].id
			# 	elif cht_thread_1:
			# 		thead_obj = ChatThread.objects.filter(sender_id = get_reciever_id.id, reciever_id = manager_id)
			# 		thread_id = cht_thread_1[0].id
			# 	else:
			# 		thead_obj = ChatThread.objects.create(sender_id = manager_id, reciever_id = get_reciever_id.id, archive = False, archive_2 = False)
			# 		thread_id = thead_obj.id
			# 		thead_obj = ChatThread.objects.filter(sender_id = manager_id, reciever_id = get_reciever_id.id)
			# 	context["thread_id"] = thread_id
			# 	if main_chat_thread:
			# 		main_chat_thread = (main_chat_thread | thead_obj).order_by('-date_updated')
			# 	else:
			# 		main_chat_thread = thead_obj

			# context["chat_thread"] = main_chat_thread

			user_obj = UserType.objects.get(user__username = reciever_email)
			if user_obj.normal_user:
				name_obj = UserDetails.objects.get(user__username = reciever_email)
				context["reciever_name"] = name_obj.name
				context["reciever_manager_id"] = name_obj.manager_id
				context["reciever_manager_timezone"] = name_obj.timezone
			elif user_obj.manager:
				name_obj = ManagerDetails.objects.get(manaager__username = reciever_email)
				context["reciever_name"] = name_obj.full_name
				context["reciever_manager_id"] = name_obj.manaager_id
				context["reciever_manager_timezone"] = name_obj.timezone
			if chat_messages:
				context['chat_messages'] = chat_messages
			else:
				context['chat_messages'] = ""
		except:
			context["user_does_not_exist"] = True

		context["userdetails"] = UserDetails.objects.get(user_id = self.request.user.id)
		context["sender_timezone"] = context["userdetails"].timezone

		context["manager_id"] = context["userdetails"].manager_id

		context["name"] = context["userdetails"].name
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = context["userdetails"].manager_id)


		posts_html = loader.render_to_string(
			'staff_chat_by_user.html',
			{'manager': context}
		)

		return HttpResponse(json.dumps(posts_html))


@method_decorator(checkloginEmployee, name='dispatch')
class StaffWindow(TemplateView):
	""" Landing page View """
	template_name = ('screen-track.html')

	def get_context_data(self, *args, **kwargs):
		# context = super(Login, self).get_context_data(*args, **kwargs)
		context = {}
		user_id = self.request.user.id
		manager_id_obj = UserDetails.objects.get(user_id = user_id)

		user_time = pytz.timezone(manager_id_obj.timezone)
		user_time_ = datetime.now(user_time)

		try:
			schedule_obj = ScheduleTiming.objects.get(user_id = self.request.user.id,  start_date__year = user_time_.year,  start_date__month  = user_time_.month,  start_date__day  = user_time_.day)
			schedule_obj_logout_time = schedule_obj.logout_time
		except:
			schedule_obj_logout_time = ""

		if schedule_obj_logout_time:
			context["countdown_timer"] = "0:00"
			context["shift_ended"] = True

		else:
			if manager_id_obj.last_countdown_timer_time:
				status_obj = OnlineStatusModel.objects.get(user_id = user_id)
				if status_obj.i_am_here:
					last_time = manager_id_obj.last_countdown_timer_time
					user_count_down_timer = int(manager_id_obj.count_timer)
					if user_time_.date() == last_time.date():
						user_time_ = parse(user_time_.strftime('%Y-%m-%d %H:%M:%S'))
						user_time_hour = (user_time_.hour * 60) + user_time_.minute + (user_time_.second/60)
						last_time_hour = (last_time.hour * 60) + last_time.minute + (last_time.second/60)
						# print(last_time.hour)
						final_minutes = user_time_hour - last_time_hour
					else:
						time_fifference = user_time_.replace(tzinfo=None) - last_time.replace(tzinfo=None)
						final_minutes = (time_fifference.total_seconds())/60

					if final_minutes > user_count_down_timer:
						countdown_timer = manager_id_obj.count_timer + ":01"
						user_time = user_time_.strftime('%Y-%m-%d %H:%M:%S')
						manager_id_obj.last_countdown_timer_time = user_time
						manager_id_obj.save()
					else:
						countdown_timer_ = user_count_down_timer - final_minutes
						countdown_timer = (str(countdown_timer_)).split(".")
						minutes = int(countdown_timer[0])
						seconds = float("."+countdown_timer[1])
						seconds = seconds*60
						if len(str(int(seconds))) == 1:
							sec = "0"+str(int(seconds))
						else:
							sec = str(int(seconds))
						countdown_timer = str(minutes)+":"+ sec
						print(countdown_timer)
					context["countdown_timer"] = countdown_timer
				else:
					status_obj.i_am_here = True
					status_obj.in_meeting = False
					status_obj.lunch_break = False
					status_obj.tea_break = False
					status_obj.offline = False
					status_obj.save()

					status = "i_am_here"
					manager_obj = User.objects.get(id = manager_id_obj.manager_id)
					url = socket_url + "/manager_notify/"+str(manager_obj.username)+"/"
					ws = create_connection(url)

					ws.send(json.dumps({'user_id': int(manager_obj.id), "status" : status, "staff_id" : self.request.user.id}))


					status_ws = create_connection(socket_url+"/chat_bxx/")
					staff_div_id = self.request.user.username
					staff_div_id = staff_div_id.replace(".", "")
					staff_div_id = staff_div_id.replace("@", "")
					status_ws.send(json.dumps({"status" : status, "staff_div_id" : staff_div_id}))

					sleep(5)
					ws.close()
					status_ws.close()
					context["countdown_timer"] = manager_id_obj.count_timer + ":01"
					user_time = user_time_.strftime('%Y-%m-%d %H:%M:%S')
					manager_id_obj.last_countdown_timer_time = user_time
					manager_id_obj.save()
			else:

				context["countdown_timer"] = manager_id_obj.count_timer + ":01"
				user_time = user_time_.strftime('%Y-%m-%d %H:%M:%S')
				manager_id_obj.last_countdown_timer_time = user_time
				manager_id_obj.save()


		context["i_am_here_countdown_timer"] = manager_id_obj.count_timer + ":01"
		context["user_details"] = manager_id_obj
		manager_id = manager_id_obj.manager_id
		context["alert_obj"] = AlertModel.objects.filter(staff_user_id_id = user_id, manager_id = manager_id).last()
		context["resources"] = AssignedDepartments.objects.filter(departments_id = manager_id_obj.department.id)

		today_date = timezone.now()
		context["tasks"] = TaskModel.objects.filter(staff_user_id_id = user_id, date_str=str(today_date.date()), acknowledge = False)
		
		today_date_task = str(today_date.date())
		today_date_task = today_date_task.split("-")
		today_date_task = today_date_task[1]+"/"+today_date_task[2]+"/"+today_date_task[0]

		# context["tasks_count"] = TaskModel.objects.filter(staff_user_id_id = user_id, date_str=today_date_task, acknowledge = False,seen_unseen = False).count()

		context["tasks_count"] = Tasks.objects.filter(task_id__staff_user_id_id = user_id, seen_unseen = False).count()

		context["email_count"] = EmailModel.objects.filter(staff_user_id = user_id, seen_unseen = False, date_str=str(today_date.date())).count()
		context["comment_count"] = CommentsModel.objects.filter(staff_user_id = user_id, seen_unseen = False).count()
		return context


class UserTasks(View):
	def post(self, request):
		try:
			user_id = request.user.id
			today_date = timezone.now()
			today_date_task = str(today_date.date())
			today_date_task = today_date_task.split("-")
			today_date_task = today_date_task[1]+"/"+today_date_task[2]+"/"+today_date_task[0]
			Tasks.objects.filter(task_id__staff_user_id_id = user_id).update(seen_unseen = True)
			# , created__gte = today_date.date()
			context = TaskModel.objects.filter(staff_user_id_id = user_id, created__gte = today_date.date()).order_by("created")
			# .values("task" ,"acknowledge","date_str","id"))


			list_ = []
			for task in context:
				dictt = {}
				dictt["acknowledge"] = task.acknowledge
				dictt["date_str"] = task.date_str
				dictt["id"] = task.id

				dictt["tasks"] = list(Tasks.objects.filter(task_id = task).values())
				list_.append(dictt)

			return HttpResponse(json.dumps(list_))
		except Exception as j:
			print(j)
			return HttpResponse(json.dumps([]))


class UserEmails(View):
	def get(self, request):
		try:
			user_id = request.user.id
			# today_date = timezone.now()
			user_obj = UserDetails.objects.get(user_id = user_id)
			user_time = pytz.timezone(user_obj.timezone)
			user_time = datetime.now(user_time)
			EmailModel.objects.filter(staff_user_id_id = int(user_id), created_staff  = user_time).update(seen_unseen = True)

			emails = list(EmailModel.objects.filter(staff_user_id_id = int(user_id), created_staff__year = user_time.year,  created_staff__month  = user_time.month,  created_staff__day  = user_time.day).values("id", "subject", "descrtiption"))

			print(emails)

			return HttpResponse(json.dumps(emails))
		except:
			return HttpResponse(json.dumps([]))

	def post(self, request):
		try:
			user_id = request.user.id
			manager_id = UserDetails.objects.get(user_id = user_id)
			manager_id = manager_id.manager_id
			today_date = timezone.now()
			email_id = request.POST.get("msg_id")
			email_message = request.POST.get("message")
			
			email_obj = EmailModel.objects.get(id = int(email_id))
			if email_obj.email_reply:
				email_obj.email_reply = email_obj.email_reply + "  :====: "+email_message
			else:
				email_obj.email_reply = email_message
			email_obj.seen_unseen = True
			email_obj.save()

			manager_obj = User.objects.get(id = manager_id)
			url = socket_url + "/manager_notify/"+str(manager_obj.username)+"/"
			ws = create_connection(url)
			ws.send(json.dumps({'email_id': int(email_id), 'email_message' : email_obj.email_reply ,"user_id" : manager_obj.id}))
			sleep(10)
			ws.close()
			return HttpResponse(1)
		except:
			return HttpResponse(0)


class StaffStatus(View):
	def post(self, request):
		try:
			staff_user_id = request.user.id
			staff_obj = UserDetails.objects.get(user_id = staff_user_id)
			manager_id = staff_obj.manager_id
			time = pytz.timezone(staff_obj.timezone)
			time = datetime.now(time)
			status = request.POST.get("status")
			check_user = UserType.objects.get(user_id = staff_user_id)

			manager_obj = ManagerDetails.objects.get(manaager_id = manager_id)
			
			time = pytz.timezone(manager_obj.timezone)
			time = datetime.now(time)

			user_obj = UserDetails.objects.get(user_id = check_user.user.id)
			user_time = pytz.timezone(user_obj.timezone)
			user_time = datetime.now(user_time)

			time = time.strftime('%Y-%m-%d %I:%M:%S')
			user_time = user_time.strftime('%Y-%m-%d %I:%M:%S')

			if check_user.normal_user == True:		
				email_obj = StaffStatusModel.objects.create(staff_user_id_id = staff_user_id, manager_id = manager_id, status = status, created_staff = user_time, created_manager = time)
				return HttpResponse(1)
			else:
				return HttpResponse(0)	
		except:
			return HttpResponse(0)


class AcknowledgedTasks(View):
	def post(self, request):
		try:
			user_id = request.POST.get("user_id")
			context = TaskModel.objects.filter(id = int(user_id)).update(acknowledge = True)
			manager_id = TaskModel.objects.filter(id = int(user_id))
			
			url = socket_url + "/task_acknowledge/"
			ws = create_connection(url)

			ws.send(json.dumps({'task_id': user_id, "user_id" : manager_id[0].manager_id}))
			sleep(5)
			ws.close()
			return HttpResponse(1)
		except Exception as j:
			print(j)
			return HttpResponse(0)


class UserAlert(View):
	def post(self, request):
		user_id = request.user.id
		today_date = timezone.now()
		context = AlertModel.objects.get(staff_user_id_id = user_id, seen_unseen = False)
		# alert_obj = AlertModel.objects.filter(staff_user_id_id = int(user_id)).update(alert = False)
		alert_message = context.alert_message
		context.seen_unseen = True
		context.alert = False
		context.delete()
		return HttpResponse(alert_message)


class StaffUserComments(View):
	def post(self, request):
		user_id = request.user.id
		today_date = timezone.now()
		context = CommentsModel.objects.filter(staff_user_id = user_id).last()

		context.seen_unseen = True
		context.save()
		return HttpResponse(context.comment)


class GetSearchedUsers(View):
	def post(self, request):
		try:
			search_query = request.POST.get('search_data')
			
			employee_name_capital = search_query.capitalize()
			employee_name_upper = search_query.upper()
			employee_name_lower = search_query.lower()

			users = UserDetails.objects.filter(name__icontains = search_query).exclude(user_id = request.user.id)
			# users_capital = UserDetails.objects.filter(name__contains = employee_name_capital).exclude(user_id = request.user.id)
			# users_upper = UserDetails.objects.filter(name__contains = employee_name_upper).exclude(user_id = request.user.id)
			# users_lower = UserDetails.objects.filter(name__contains = employee_name_lower).exclude(user_id = request.user.id)

			# users = users | users_capital | users_upper |users_lower
			users = users


			# managers_name_capital = search_query.capitalize()
			# managers_name_upper = search_query.upper()
			# managers_name_lower = search_query.lower()

			managers = (ManagerDetails.objects.filter(full_name__icontains = search_query))
			# managers_capital = (ManagerDetails.objects.filter(full_name__contains = managers_name_capital))
			# managers_upper = (ManagerDetails.objects.filter(full_name__contains = managers_name_upper))
			# managers_lower = (ManagerDetails.objects.filter(full_name__contains = managers_name_lower))
			
			# managers = managers | managers_capital | managers_upper | managers_lower
			managers = managers

			final_users = list(users.values('name','user__username')) + list(managers.values('full_name','manaager__username'))
			return HttpResponse(json.dumps(final_users))
		except:
			return HttpResponse(0)


class ArchiveChat(View):
	def post(self, request):
		user_id = request.user.id
		user_email = request.POST.get("user_mail")
		try:
			thread_obj = ChatThread.objects.filter(sender__username = request.user.username, reciever__username = user_email)
			if thread_obj:
				ChatThread.objects.filter(sender__username = request.user.username, reciever__username = user_email).update(archive = True)
			else:
				ChatThread.objects.filter(reciever__username = request.user.username, sender__username = user_email).update(archive_2 = True)
			return HttpResponse(1)
		except Exception as h:
			return HttpResponse(0)


class UserOnlineStatus(View):
	"""docstring for UserStatus"""

	def post(self, request):
		try:
			user_status = request.POST.get("user_status")
			user_id = request.user.id
			user_obj = OnlineStatusModel.objects.filter(user_id = user_id)
			time = timezone.now()
			manager_id_obj = UserDetails.objects.get(user_id = user_id)
			user_time = pytz.timezone(manager_id_obj.timezone)
			user_time_ = datetime.now(user_time)
			user_time = user_time_.strftime('%Y-%m-%d %H:%M:%S')
			if user_status == "i_am_here":				
				if user_obj:
					
					UserDetails.objects.filter(user_id = user_id).update(last_countdown_timer_time = user_time)
					user_obj = OnlineStatusModel.objects.filter(user_id = user_id).update(i_am_here = True, in_meeting = False, lunch_break = False, tea_break = False, offline = False, time = user_time)


			if user_status == "in_meeting":
				if user_obj:
					user_obj = OnlineStatusModel.objects.filter(user_id = user_id).update(i_am_here = False, in_meeting = True, lunch_break = False, tea_break = False, offline = False, time = user_time)

			if user_status == "lunch_break":
				if user_obj:
					user_obj = OnlineStatusModel.objects.filter(user_id = user_id).update(i_am_here = False, in_meeting = False, lunch_break = True, tea_break = False, offline = False, time = user_time)

			if user_status == "tea_break":
				if user_obj:
					user_obj = OnlineStatusModel.objects.filter(user_id = user_id).update(i_am_here = False, in_meeting = False, lunch_break = False, tea_break = True, offline = False, time = user_time)	

			if user_status == "offline":
				if user_obj:
					user_obj = OnlineStatusModel.objects.filter(user_id = user_id).update(i_am_here = False, in_meeting = False, lunch_break = False, tea_break = False, offline = True, time = user_time)	

			online_status = OnlineStatusModel.objects.get(user_id = user_id)
			if online_status.i_am_here:
				status = "i_am_here"
			elif online_status.in_meeting:
				status = "in_meeting"
			elif online_status.lunch_break:
				status = "lunch_break"
			elif online_status.tea_break:
				status = "tea_break"
			elif online_status.offline:
				status = "offline"

			manager_id_obj = UserDetails.objects.get(user_id = online_status.user.id)
			manager_obj = User.objects.get(id = manager_id_obj.manager_id)
			url = socket_url+"/manager_notify/"+str(manager_obj.username)+"/"
			ws = create_connection(url)

			ws.send(json.dumps({'user_id': int(manager_obj.id), "status" : status, "staff_id" : online_status.user.id}))
			
			status_ws = create_connection(socket_url+"/chat_bxx/")
			staff_div_id = online_status.user.username
			staff_div_id = staff_div_id.replace(".", "")
			staff_div_id = staff_div_id.replace("@", "")
			status_ws.send(json.dumps({"status" : status, "staff_div_id" : staff_div_id}))
			sleep(5)
			status_ws.close()
			ws.close()
			return HttpResponse(1)
		except:
			return HttpResponse(0)
	

class StaffProfile(TemplateView):
	template_name = "staff_profile.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		employee_id = self.request.user.id

		user_details = UserDetails.objects.get(user_id = employee_id)
		try:
			context["user_details"]	= user_details
		except:
			context["user_details"]	= False
		context["departments"] = list(Departments.objects.all().values())
		return context


class EndShift(View):
	def post(self, request):
		try:
			user_obj = UserDetails.objects.get(user_id = request.user.id)
			user_time = pytz.timezone(user_obj.timezone)
			user_time_ = datetime.now(user_time)
			user_time = user_time_.strftime('%Y-%m-%d %I:%M:%S')

			schedule_obj = ScheduleTiming.objects.filter(user_id = request.user.id, login_time__year = user_time_.year,  login_time__month  = user_time_.month,  login_time__day  = user_time_.day).last()
			if schedule_obj.logout_time:
				return HttpResponse(5)
			else:
				ScheduleTiming.objects.filter(user_id = request.user.id, login_time__year = user_time_.year,  login_time__month  = user_time_.month,  login_time__day  = user_time_.day).update(logout_time = user_time)
				# schedule_obj.save()
			return HttpResponse(1)
		except Exception as h:
			print(h)
			return HttpResponse(0)


class StaffStatusRuntime(View):
	def post(self, request):
		try:



			staff_id = request.POST.get("user_id")
			status = request.POST.get("user_status")
			user_obj = UserDetails.objects.get(user_id = int(staff_id))
			user_time = pytz.timezone(user_obj.timezone)
			user_time_ = datetime.now(user_time)
			user_time = user_time_.strftime('%Y-%m-%d %H:%M:%S')

			# print(status)
			schedule_obj = ScheduleTiming.objects.filter(user_id = int(staff_id), start_date__year = user_time_.year,  start_date__month  = user_time_.month,  start_date__day  = user_time_.day)

			obj = OnlineStatusModel.objects.get(user_id = int(staff_id))
			if status == "i_am_here":
				obj.i_am_here = True
				obj.in_meeting = False
				obj.lunch_break = False
				obj.tea_break = False
				obj.offline = False
				for ob in schedule_obj:
					ob.online_time = ob.online_time + 1
					ob.save()
			elif status == "in_meeting":
				obj.in_meeting = True
				obj.i_am_here = False
				obj.lunch_break = False
				obj.tea_break = False
				obj.offline = False
				for ob in schedule_obj:
					ob.break_time = ob.break_time + 1
					ob.save()
			elif status == "lunch_break":
				obj.lunch_break = True
				obj.in_meeting = False
				obj.i_am_here = False
				obj.tea_break = False
				obj.offline = False
				for ob in schedule_obj:
					ob.break_time = ob.break_time + 1
					ob.save()
			elif status == "tea_break":
				obj.tea_break = True
				obj.lunch_break = False
				obj.in_meeting = False
				obj.i_am_here = False
				obj.offline = False
				for ob in schedule_obj:
					ob.break_time = ob.break_time + 1
					ob.save()
			else:
				obj.offline = True
				obj.tea_break = False
				obj.lunch_break = False
				obj.in_meeting = False
				obj.i_am_here = False
				for ob in schedule_obj:
					ob.offline_time = ob.offline_time + 1
					ob.save()
			obj.time = user_time
			obj.save()

			# obj.lunch_break = False
			# obj.tea_break = False
			# obj.offline = False
			return HttpResponse(1)
		except Exception as i:
			print(i)
			return HttpResponse(0)


class OpenResource(View):
	def post(self, request):
		try:
			user_id = request.POST.get("user_id")
			user_obj = UserDetails.objects.get(user_id = int(user_id))
			context = {}
			context["resources"] = AssignedDepartments.objects.filter(departments_id = user_obj.department.id)
			posts_html = loader.render_to_string(
				'resource_staff.html',
				{'user': context}
			)
			return HttpResponse(json.dumps(posts_html))
		except:
			return HttpResponse(0)









# Manager dashboard
@method_decorator(checkloginManager, name='dispatch')
class ManagerDashboard(TemplateView):
	""" Landing page View """
	template_name = ('manager_dashboard.html')

	def get_context_data(self, *args, **kwargs):
		context = {}
		user_id = self.request.user.id
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = user_id)
		context["timezones"] = all_timezones
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = user_id)
		context["manager_count"] = UserDetails.objects.filter(manager_id = user_id).count()

		context["manager_emails"] = EmailModel.objects.filter(manager_id = user_id).order_by("-id")[0:5]
		
		context["timezone1_count"] = UserDetails.objects.filter(timezone = context["user_timezones"].timezone1, manager_id = user_id).count()
		context["timezone2_count"] = UserDetails.objects.filter(timezone = context["user_timezones"].timezone2, manager_id = user_id).count()
		context["timezone3_count"] = UserDetails.objects.filter(timezone = context["user_timezones"].timezone3, manager_id = user_id).count()
		context["timezone4_count"] = UserDetails.objects.filter(timezone = context["user_timezones"].timezone4, manager_id = user_id).count()

		users_list = list(UserDetails.objects.filter(manager_id = user_id).values_list('user_id',flat=True))
		chat_thread = ChatThread.objects.filter(sender_id__in = users_list, archive = False, date_updated__isnull = False)
		chat_thread_1 = ChatThread.objects.filter(reciever_id__in = users_list, archive_2 = False, date_updated__isnull = False)
		chat_thread_2 = ChatThread.objects.filter(sender_id = user_id, archive = False, date_updated__isnull = False)
		chat_thread_3 = ChatThread.objects.filter(reciever_id = user_id, archive_2 = False, date_updated__isnull = False)
		context["chat_thread"] = (chat_thread | chat_thread_1 | chat_thread_2 | chat_thread_3).order_by('-date_updated')

		user_obj = ManagerDetails.objects.get(manaager_id = user_id)
		user_time = pytz.timezone(user_obj.timezone)
		user_time_ = datetime.now(user_time)
		user_time = user_time_.strftime('%Y-%m-%d %H:%M:%S')
		online_status = OnlineStatusModel.objects.get(user_id = user_id)
		if not online_status.i_am_here:
			online_status.i_am_here = True
			online_status.in_meeting = False
			online_status.lunch_break = False
			online_status.tea_break = False
			online_status.offline = False
			online_status.time = user_time
			online_status.save()
			
			status = "i_am_here"
			
			status_ws = create_connection(socket_url+"/chat_bxx/")
			staff_div_id = online_status.user.username
			staff_div_id = staff_div_id.replace(".", "")
			staff_div_id = staff_div_id.replace("@", "")
			status_ws.send(json.dumps({"status" : status, "staff_div_id" : staff_div_id}))
			sleep(4)
			status_ws.close()
		
		return context


class UnblockStaff(View):

	def post(self, request):
		user_id = request.POST.get("user_id")
		user_type = UserType.objects.filter(user_id = int(user_id), normal_user = True)
		
		try:
			if user_type:
				unblock_obj = InvalidAttempts.objects.get(user_id = user_id)
				unblock_obj.blocked = False
				unblock_obj.attempts = 0
				unblock_obj.save()
				return HttpResponse(1)
			else:
				return HttpResponse(0)
		except:
			return HttpResponse(0)


@method_decorator(checkloginManager, name='dispatch')
class AddStaffMember(TemplateView):
	template_name = ('add-employee.html')
	
	def get_context_data(self, *args, **kwargs):
		context = {}
		user_id = self.request.user.id
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = user_id)
		context["departments"] = list(Departments.objects.all().values())
		context["cities"] = Cities.objects.all()
		context["timezones"] = all_timezones
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = user_id)
		context["functions"] = Functions.objects.all()
		context["designations"] = Designation.objects.all()
		return context
	
	def post(self, request):
		try:
			name = request.POST.get("name")
			email1 = request.POST.get("email1")
			email2 = request.POST.get("email2")
			phone1 = request.POST.get("phone1")
			phone2 = request.POST.get("phone2")
			password = request.POST.get("password")
			dummy_specification_line = request.POST.get("dummy_specification_line")
			comment = request.POST.get("comment")
			staff_timezone = request.POST.get("staff_timezone")
			city = request.POST.get("city")
			countdown_timer = request.POST.get("countdown_timer")
			function = request.POST.get("function")
			department = request.POST.get("department")
			department_id = request.POST.get("department_id")
			manager_id = request.POST.get("manager_id")
			designation = request.POST.get("designation")
			user = User.objects.filter(username = email1)
			time = timezone.now()
			if not user:
				user = User.objects.create(username = email1, email = email1, is_superuser = False)
				user.set_password(password)
				user.save()
				InvalidAttempts.objects.create(user_id = user.id, blocked = False, attempts = 0)
				department_obj = Departments.objects.get(id = int(department_id))
				UserType.objects.create(user_id = user.id, normal_user = True, manager = False)
				UserDetails.objects.create(user_id = user.id, manager_id = manager_id, email2 = email2, phone_no_1 = phone1, phone_no_2 = phone2, timezone = staff_timezone, city = city, department_id = department_obj.id, count_timer = countdown_timer, it_equipment_specification = dummy_specification_line, comment = comment, function = function, name = name, designation = designation)
				AlertModel.objects.create(staff_user_id_id = user.id, manager_id = manager_id)
				OnlineStatusModel.objects.create(user_id = user.id, i_am_here = False, in_meeting = False, lunch_break = False, tea_break = False, offline = True, time = time.now())
				return HttpResponse(1)
			else:
				return HttpResponse("already_exist")

		except:
			return HttpResponse(0)


class DeleteStaffMember(View):
	def post(self, request):
		try:
			user_id = request.POST.get("user_id")
			user = User.objects.filter(id = user_id)
			user_type_check = UserType.objects.filter(user_id = user.id, normal_user = True)
			if user_type_check:
				user.delete()
				return HttpResponse(1)
			else:
				return HttpResponse("not_a_staff_user")

		except:	
			return HttpResponse(0)


class ManagerClock(View):
	def post(self, request):
		timezone1 = request.POST.get("timezone1")
		timezone2 = request.POST.get("timezone2")
		timezone3 = request.POST.get("timezone3")
		timezone4 = request.POST.get("timezone4")
		manager_id = request.user.id
		try:
			manager_obj = ManagerTimezones.objects.filter(manager_id = manager_id)
			if manager_obj:
				ManagerTimezones.objects.filter(manager_id = manager_id).update(timezone1 = timezone1, timezone2 = timezone2, timezone3 = timezone3, timezone4 = timezone4)
			else:
				ManagerTimezones.objects.create(manager_id = manager_id, timezone1 = timezone1, timezone2 = timezone2, timezone3 = timezone3, timezone4 = timezone4)
			return HttpResponse(1)		
		except:	
			return HttpResponse(0)


class UserComment(View):
	def post(self, request):
		try:
			manager_id = request.user.id
			staff_user_id = request.POST.get("user_id")
			comment = request.POST.get("comment")

			check_user = UserType.objects.get(user_id = staff_user_id)

			if check_user.normal_user == True:			
				comment_obj = CommentsModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id)
				if comment_obj:
					CommentsModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id).update(comment = comment, seen_unseen = False)
				else:
					CommentsModel.objects.create(staff_user_id_id = int(staff_user_id), comment = comment, manager_id = manager_id)
				return HttpResponse(1)
			else:
				return HttpResponse(0)	
		except:
			return HttpResponse(0)


class Email(View):
	def post(self, request):
		try:			
			manager_id = request.user.id
			subject = request.POST.get("email_subject")
			descrtiption = request.POST.get("email_description")
			to_email = request.POST.get("to_email")
			from_email = request.POST.get("from_email")
			check_user = UserType.objects.get(user__email = to_email)
			manager_obj = ManagerDetails.objects.get(manaager_id = manager_id)
			
			time = pytz.timezone(manager_obj.timezone)
			time = datetime.now(time)

			user_obj = UserDetails.objects.get(user_id = check_user.user.id)
			user_time = pytz.timezone(user_obj.timezone)
			user_time = datetime.now(user_time)


			time = time.strftime('%Y-%m-%d %I:%M:%S')
			user_time = user_time.strftime('%Y-%m-%d %I:%M:%S')


			if check_user.normal_user == True:
				EmailModel.objects.create(staff_user_id_id = int(check_user.user.id), manager_id = manager_id, subject = subject, descrtiption = descrtiption, to_email = to_email, from_email = from_email, date_str = str(time), created_manager = time, from_name = manager_obj.full_name, to_name = user_obj.name, created_staff  = user_time)

				email_count = EmailModel.objects.filter(staff_user_id_id = int(check_user.user.id),seen_unseen = False).count()
				url = socket_url + "/channels_url/"+str(check_user.user.username)+"/"
				ws = create_connection(url)
				ws.send(json.dumps({'user_id': int(check_user.user.id),'task_count': 0, "alert_count" : 0, "email_count" : email_count, "comment_count" : 0}))
				sleep(5)
				ws.close()
				return HttpResponse(1)
			else:
				return HttpResponse(0)	
		except:
			return HttpResponse(0)


class Alert(View):
	def post(self, request):
		try:
			manager_id = request.user.id
			staff_user_id = request.POST.get("user_id")
			alert_message = request.POST.get('alert_message')

			check_user = UserType.objects.get(user_id = staff_user_id)

			if check_user.normal_user == True:			
				alert_obj = AlertModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id)
				if alert_obj:
					AlertModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id).update(alert = True, alert_message = alert_message, seen_unseen = False)
				else:
					AlertModel.objects.create(staff_user_id_id = int(staff_user_id), manager_id = manager_id, alert = True, alert_message = alert_message, seen_unseen = False)
						

				alert_count = AlertModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id,seen_unseen = False).count()

				url = socket_url + "/channels_url/"+str(check_user.user.username)+"/"
				ws = create_connection(url)
				ws.send(json.dumps({'user_id': int(staff_user_id),'task_count' : 0, "alert_count" : alert_count,'alert_message' : alert_message, "email_count" : 0, "comment_count" : 0}))
				sleep(5)
				ws.close()
				return HttpResponse(1)
			else:
				return HttpResponse(0)	
		except:
			return HttpResponse(0)

	# def get(self, request):
	# 	try:
	# 		user_id = request.user.id
	# 		alert_obj = AlertModel.objects.filter(staff_user_id_id = int(user_id)).update(alert = False)
	# 		return HttpResponse(1)
	# 	except:
	# 		return HttpResponse(0)		


class TaskAssign(View):
	def post(self, request):
		try:
			today_date = timezone.now()
			manager_id = request.user.id
			staff_user_id = request.POST.get("user_id")
			task = request.POST.get("task")
			task_date = request.POST.get("date")
			check_user = UserType.objects.get(user_id = staff_user_id)
			username = check_user.user.username

			if check_user.normal_user == True:			
				task_obj = TaskModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id, date_str = task_date)
				if task_obj:
					task_mo = TaskModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id, date_str = task_date).last()

					TaskModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id, date_str = task_date).update(acknowledge = False)

					Tasks.objects.create(task_id = task_mo, task = task, seen_unseen = False)
					# tasks_obj = task_mo
					# task_mo = task_mo.task
					# TaskModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id, date_str = task_date).update(task = task_mo+" ,,, "+task, seen_unseen = False, acknowledge = False)
				else:
					tasks_obj = TaskModel.objects.create(staff_user_id_id = int(staff_user_id), manager_id = manager_id, date_str = task_date, created = parse(task_date), seen_unseen = False)
					Tasks.objects.create(task_id = tasks_obj, task = task, seen_unseen = False)


				task_count = Tasks.objects.filter(task_id__staff_user_id_id = int(staff_user_id), seen_unseen = False).count()
				# task_count = TaskModel.objects.filter(staff_user_id_id = int(staff_user_id), manager_id = manager_id,seen_unseen = False).count()
				url = socket_url + "/channels_url/"+str(check_user.user.username)+"/"
				ws = create_connection(url)
				ws.send(json.dumps({'user_id': int(staff_user_id),'task_count' : task_count, "alert_count" : 0, "email_count" : 0, "comment_count" : 0}))
				sleep(5)
				ws.close()
				
				return HttpResponse(1)
			else:
				return HttpResponse(0)	
		except Exception as k:
			print(k)
			return HttpResponse(0)


@method_decorator(checkloginManager, name='dispatch')
class StaffEmployeeProfile(TemplateView):
	template_name = "employee.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		employee_id = self.request.GET.get('employee_id',None)
		manager_id = self.request.user.id
		context["timezones"] = all_timezones
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)

		if employee_id:
			employee_id = int(employee_id)
			context["status_obj"] = StaffStatusModel.objects.filter(staff_user_id_id = employee_id, manager_id = manager_id).order_by("-id")
			context["employee_id"] = int(employee_id)
		else:
			context["nodata_found"]	= True
		try:
			context["user_details"]	= UserDetails.objects.get(user_id = employee_id)
			context["assigned_resources"] = AssignedDepartments.objects.filter(departments_id = context["user_details"].department.id)[0:5]
			reciever_email = context["user_details"].user.username
			context["reciever_email"] = reciever_email
			reciever_div_id = reciever_email.replace(".","")
			context["reciever_div_id"] = reciever_div_id.replace("@","")
			user_div_id = (self.request.user.username).replace(".","")
			context["user_div_id"] = user_div_id.replace("@","")
			get_reciever_id = context["user_details"].user.id
			context["reciever_id"] = get_reciever_id
			context["reciever_name"] = context["user_details"].name
		except:
			context["user_details"]	= False
			context["assigned_resources"] = False 
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)
		context["unblock_obj"] = InvalidAttempts.objects.filter(user_id = employee_id, blocked = True)
		
		context["emails"] = EmailModel.objects.filter(staff_user_id_id = employee_id, manager_id = manager_id)

		sender_obj = ChatMessage.objects.filter(sender_id = employee_id, reciever_id = manager_id)
		reciever_obj = ChatMessage.objects.filter(sender_id = manager_id, reciever_id = employee_id)

		if reciever_obj or sender_obj:
			context["thread_id"] = (reciever_obj | sender_obj)[0].thread.id
		else:
			chat_thread_obj = ChatThread(sender_id = employee_id, reciever_id = manager_id)
			chat_thread_obj.save()
			context["thread_id"] = chat_thread_obj.id

		context["chat_messages"] = (reciever_obj | sender_obj)
		return context


@method_decorator(checkloginManager, name='dispatch')
class Resources(TemplateView):
	template_name = "resource.html"

	def get_context_data(self, *args, **kwargs):
		try:
			context = {}
			sort_by = self.request.GET.get('sort_by', None)
			search_name = self.request.GET.get('search_name', None)
			user_id = self.request.user.id

			if sort_by and search_name:
				sort_by_obj = SavedDocumentModel.objects.filter(user_id = user_id).order_by("-"+str(sort_by))
				name_obj = SavedDocumentModel.objects.filter(user_id = user_id, name__icontains = search_name).order_by("-"+str(sort_by))
				context["documents"] = sort_by_obj & name_obj
				context["query_str"] = sort_by
				context["seached_by"] = search_name
			elif sort_by:
				sort_by_obj = SavedDocumentModel.objects.filter(user_id = user_id).order_by("-"+str(sort_by))
				context["documents"] = sort_by_obj
				context["query_str"] = sort_by

			elif search_name:
				name_obj = SavedDocumentModel.objects.filter(user_id = user_id, name__icontains = search_name)
				context["documents"] = name_obj
				context["seached_by"] = search_name

			else:
				context["documents"] = SavedDocumentModel.objects.filter(user_id = user_id)
				context["query_str"] = ""
			
			context["departments"] = list(Departments.objects.all().values())
			context["user_timezones"] = ManagerTimezones.objects.get(manager_id = user_id)
			context["timezones"] = all_timezones
			context["manager_details"] = ManagerDetails.objects.get(manaager_id = user_id)

			return context
		except:
			return {}


@method_decorator(checkloginManager, name='dispatch')
class EmailListing(TemplateView):
	template_name = "email-listing.html"
	
	def get_context_data(self, *args, **kwargs):
		context = {}
		manager_id = self.request.user.id
		context["timezones"] = all_timezones
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)
		
		manager_username = self.request.user.username

		employee_name = self.request.GET.get("emp_name" , None)
		if employee_name:
			employee_name_capital = employee_name.capitalize()
			employee_name_upper = employee_name.upper()
			employee_name_lower = employee_name.lower()

			user_details_obj =  EmailModel.objects.filter(Q(manager_id = manager_id, to_name__icontains = employee_name) | Q(manager_id = manager_id, from_email__icontains = employee_name) | Q(manager_id = manager_id, email_reply__icontains = employee_name) | Q(manager_id = manager_id, subject__icontains = employee_name) | Q(manager_id = manager_id, descrtiption__icontains = employee_name))

			# user_details_obj_capital =  EmailModel.objects.filter(Q(manager_id = manager_id, to_name__contains = employee_name_capital) | Q(manager_id = manager_id, from_email__contains = employee_name_capital) | Q(manager_id = manager_id, email_reply__contains = employee_name_capital) | Q(manager_id = manager_id, subject__contains = employee_name_capital) | Q(manager_id = manager_id, descrtiption__contains = employee_name_capital))

			# user_details_obj_upper =  EmailModel.objects.filter(Q(manager_id = manager_id, to_name__contains = employee_name_upper) | Q(manager_id = manager_id, from_email__contains = employee_name_upper) | Q(manager_id = manager_id, email_reply__contains = employee_name_upper) | Q(manager_id = manager_id, subject__contains = employee_name_upper) | Q(manager_id = manager_id, descrtiption__contains = employee_name_upper))

			# user_details_obj_lower =  EmailModel.objects.filter(Q(manager_id = manager_id, to_name__contains = employee_name_lower) | Q(manager_id = manager_id, from_email__contains = employee_name_lower) | Q(manager_id = manager_id, email_reply__contains = employee_name_lower) | Q(manager_id = manager_id, subject__contains = employee_name_lower) | Q(manager_id = manager_id, descrtiption__contains = employee_name_lower))
			
			# user_emails_obj = user_details_obj | user_details_obj_capital | user_details_obj_upper | user_details_obj_lower
			user_emails_obj = user_details_obj
			
			context["emails_count"] = user_emails_obj.count()
			context["employee_name"] = employee_name
			user_emails_obj = user_emails_obj.order_by('-id')
		else:	
			user_emails_obj = EmailModel.objects.filter(manager_id = manager_id).order_by('-id')
			context["emails_count"] = EmailModel.objects.filter(manager_id = manager_id).count()
		paginator = Paginator(user_emails_obj, 25)

		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context["page_obj"] = page_obj

		return context


@method_decorator(checkloginManager, name='dispatch')
class EmployeeListing(TemplateView):
	template_name = "employee-listing.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		manager_id = self.request.user.id
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)
		context["timezones"] = all_timezones
		

		employee_name = self.request.GET.get("emp_name" , None)
		if employee_name:
			employee_name_capital = employee_name.capitalize()
			employee_name_upper = employee_name.upper()
			employee_name_lower = employee_name.lower()

			user_details_obj =  UserDetails.objects.filter(Q(manager_id = manager_id, name__icontains = employee_name) | Q(manager_id = manager_id, department__departments__icontains = employee_name) | Q(manager_id = manager_id, city__icontains = employee_name) | Q(manager_id = manager_id, function__icontains = employee_name)).order_by("-id")

			# user_details_obj_capital =  UserDetails.objects.filter(Q(manager_id = manager_id, name__contains = employee_name_capital) | Q(manager_id = manager_id, department__departments__contains = employee_name_capital) | Q(manager_id = manager_id, city__contains = employee_name_capital) | Q(manager_id = manager_id, function__contains = employee_name_capital)).order_by("-id")

			# user_details_obj_upper =  UserDetails.objects.filter(Q(manager_id = manager_id, name__contains = employee_name_upper) | Q(manager_id = manager_id, department__departments__contains = employee_name_upper) | Q(manager_id = manager_id, city__contains = employee_name_upper) | Q(manager_id = manager_id, function__contains = employee_name_upper)).order_by("-id")

			# user_details_obj_lower =  UserDetails.objects.filter(Q(manager_id = manager_id, name__contains = employee_name_lower) | Q(manager_id = manager_id, department__departments__contains = employee_name_lower) | Q(manager_id = manager_id, city__contains = employee_name_lower) | Q(manager_id = manager_id, function__contains = employee_name_lower)).order_by("-id")
			
			# user_details_obj = user_details_obj | user_details_obj_capital | user_details_obj_upper | user_details_obj_lower
			user_details_obj = user_details_obj
			context["emp_count"] =  user_details_obj.count()
			context["employee_name"] = employee_name
		else:
			user_details_obj =  UserDetails.objects.filter(manager_id = manager_id).order_by("-id")
			context["emp_count"] =  UserDetails.objects.filter(manager_id = manager_id).count()
		paginator = Paginator(user_details_obj, 25)
		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context["page_obj"] = page_obj
		return context


class SaveDocument(View):
	def post(self,request):
		user_id = request.user.id
		try:
			file = request.FILES["file"]
			extension = (file.name).split(".")
			extension = extension[-1]
			if not os.path.exists(settings.DEFAULT_STORAGE+"/"+str(user_id)):
				os.makedirs(settings.DEFAULT_STORAGE+"/"+str(user_id))
				file_name = default_storage.save(settings.DEFAULT_STORAGE+"/"+str(user_id)+"/"+str(file.name), file)
			else:
				file_name = default_storage.save(settings.DEFAULT_STORAGE+"/"+str(user_id)+"/"+str(file.name), file)
			manager_obj = SavedDocumentModel.objects.filter(user_id = user_id, name = file.name)

			manager_obdj = ManagerDetails.objects.get(manaager_id = user_id)
			
			time = pytz.timezone(manager_obdj.timezone)
			time = datetime.now(time)

			time = time.strftime('%Y-%m-%d %I:%M:%S')

			if manager_obj:
				if extension == "doc":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, doc = True, pptx = False, xlsx = False)
				elif extension == "docx":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, docx = True, pptx = False, xlsx = False, png = False, jpg = False)
				elif extension == "pdf":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, pdf = True, pptx = False, xlsx = False, png = False, jpg = False)
				elif extension == "ppt":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, ppt = True, pptx = False, xlsx = False, png = False, jpg = False)
				elif extension == "csv":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, csv = True, pptx = False, xlsx = False, png = False, jpg = False)
				elif extension == "jpeg":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, jpeg = True, pptx = False, xlsx = False, png = False, jpg = False)
				elif extension == "xls":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, xls = True, pptx = False, xlsx = False, png = False, jpg = False)
				elif extension == "pptx":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, xls = False, pptx = True, xlsx = False, png = False, jpg = False)
				elif extension == "xlsx":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, xls = False, pptx = False, xlsx = True, png = False, jpg = False)
				elif extension == "png":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, xls = False, pptx = False, xlsx = True, png = True, jpg = False)	
				elif extension == "jpg":
					SavedDocumentModel.objects.filter(user_id = user_id, name = file.name).update(path = "/media/"+str(user_id)+"/"+str(file.name), extension = extension, xls = False, pptx = False, xlsx = True, png = False, jpg = True)	
				return HttpResponse(5)
			else:
				if extension == "doc":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, doc = True, xlsx = False, png = False, jpg = False, created = time)
				elif extension == "docx":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, docx = True, xlsx = False, png = False, jpg = False, created = time)
				elif extension == "pdf":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, pdf = True, xlsx = False, png = False, jpg = False, created = time)
				elif extension == "ppt":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, ppt = True, xlsx = False, png = False, jpg = False, created = time)
				elif extension == "csv":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, csv = True, xlsx = False, png = False, jpg = False, created = time)
				elif extension == "jpeg":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, jpeg = True, xlsx = False, png = False, jpg = False, created = time)
				elif extension == "xls":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, xls = True, xlsx = False, png = False, jpg = False, created = time)
				elif extension == "pptx":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, pptx = True, xlsx = False, png = False, jpg = False, created = time)
				elif extension == "xlsx":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, pptx = False, xlsx = True, png = False, jpg = False, created = time)
				elif extension == "png":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, pptx = False, xlsx = True, png = True, jpg = False, created = time)
				elif extension == "jpg":
					SavedDocumentModel.objects.create(user_id = user_id, path = "/media/"+str(user_id)+"/"+str(file.name), name = file.name, extension = extension, pptx = False, xlsx = True, png = False, jpg = True, created = time)


			return HttpResponse(1)

		except Exception as j:
			print(j)
			return HttpResponse(0)


class AssignDepartment(View):
	def get(self, request):
		try:
			value = request.GET.get("data")
			split_val = value.split(" && ")
			name = split_val[1]
			path = split_val[0]
			dept_obj = list(AssignedDepartments.objects.filter(name = name, path = path).values("departments__departments", "id"))
			return HttpResponse(json.dumps(dept_obj))
		except:
			return HttpResponse(2)

	def post(self, request):
		try:
			attr = request.POST.get("attr")
			assign_department = request.POST.get("assign_department")
			assign_department_id = request.POST.get("assign_department_id")
			name_split = attr.split(" && ")
			name = name_split[1]
			path = name_split[0]
			dept_obj = AssignedDepartments.objects.filter(departments_id = assign_department_id, name = name)
			if dept_obj:
				return HttpResponse(5)
			else:	
				AssignedDepartments.objects.create(departments_id = assign_department_id, name = name, path = path)
				return HttpResponse(1)
		except Exception as f:
			return HttpResponse(0)


class RemoveDepartment(View):
	def post(self, request):
		try:
			resource_id = request.POST.get('resource_id')
			resource_obj = AssignedDepartments.objects.filter(id = int(resource_id))
			resource_obj.delete()
			return HttpResponse(1)
		except:
			return HttpResponse(0)


class StaffResource(View):
	def get(self, request):
		user_id = request.user.id
		user_obj = UserDetails.objects.get(user_id = user_id)
		department = user_obj.department.id
		department_data = list(AssignedDepartments.objects.filter(departments_id = department).values())
		return HttpResponse(json.dumps(department_data))


class DeleteResource(View):
	def post(self, request):
		resource_id = request.POST.get("resource_id")
		try:
			user_id = request.user.id
			doc_obj = SavedDocumentModel.objects.get(id = int(resource_id))
			AssignedDepartments.objects.filter(name = doc_obj.name, path = doc_obj.path).delete()
			doc_obj.delete()
			return HttpResponse(1)
		except:	
			return HttpResponse(0)


class DeleteTask(View):
	def post(self, request):
		task_id = request.POST.get("task_id")
		try:
			task_count_ = Tasks.objects.get(id=int(task_id))
			task_count = Tasks.objects.filter(task_id_id = int(task_count_.task_id.id)).count()
			if task_count == 1:
				TaskModel.objects.filter(id=task_count_.task_id.id).delete()
			else:
				Tasks.objects.filter(id = int(task_id)).delete()
			return HttpResponse(1)
		except Exception as r:
			print(r)	
			return HttpResponse(0)


class ChangeStaffPassword(View):
	def post(self, request):
		try:
			email = request.POST.get("email")
			new_pass = request.POST.get("password")
			user_obj = User.objects.get(username = email)
			user_obj.set_password(new_pass)
			user_obj.save()
			return HttpResponse(1)
		except:
			return HttpResponse(0)


@method_decorator(checkloginManager, name='dispatch')
class ManagerProfile(TemplateView):
	template_name = "manager-profile.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		manager_id = self.request.user.id
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
		context["timezones"] = all_timezones
		context["documents"] = SavedDocumentModel.objects.filter(user_id = manager_id).values()
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)
		context["departments"] = Departments.objects.all()
		return context

	def post(self, request):
		# print(request.POST)
		try:
			imgdata = request.POST.get("profile_pic")
			user_id = request.user.id
			if imgdata:
				image_name = str(int(time.time()))
				image = imgdata.split(";base64,")
				extens = image[0]
				ext = extens.split("/")
				extension = ext[1]
				base_image = image[1]
				b_image = base64.b64decode(base_image)
				filename = image_name + "." + extension
				
				image_path_to_saved = settings.PROFILE_IMAGE_PATH + filename
				file_path = settings.PROFILE_IMAGE_PATH + image_name

				old_profile = ManagerDetails.objects.get(manaager_id = user_id)
				if "/static/img/admin-demo.png" in old_profile.profile_pic.name:
					pass
				else:
					try:
						pic = old_profile.profile_pic.name
						pic = pic.split("profile_pictures/")

						os.remove(settings.PROFILE_IMAGE_PATH+pic[-1])
					except:
						pass

				with open(image_path_to_saved, 'wb') as f:
					f.write(b_image)

				profile_pic_model_path = image_path_to_saved.split("/static")
				ManagerDetails.objects.filter(manaager_id = user_id).update(profile_pic = "/static"+profile_pic_model_path[-1])
				print(profile_pic_model_path)
			return HttpResponse(1)
		except Exception as t:
			print(t)
			return HttpResponse(0)


class SchedulerTime(View):
	def post(self, request):
		try:
			start_date = request.POST.get('start_date')
			end_date = request.POST.get('end_date')
			start_time = request.POST.get('start_time')
			start_time = start_time.replace(" : ",":")
			end_time = request.POST.get('end_time')
			end_time = end_time.replace(" : ",":")
			start_date = parse(start_date)
			end_date = parse(end_date)
			start_time = parse(start_time)
			end_time = parse(end_time)
			user_id = request.user.id
			staff_id = request.POST.get('staff_id')
			if start_date == end_date:
				if start_time == end_time:
					return HttpResponse("Time should not be same")
				elif end_time < start_time:
					return HttpResponse("End time should not be less")
				else:

					schedule_obj = ScheduleTiming.objects.filter(manager_id = user_id, user_id = int(staff_id),  start_date__year = start_date.year,  start_date__month  = start_date.month,  start_date__day  = start_date.day)
					if schedule_obj:
							schedule_obj.update(end_date = end_date, start_time = start_time, end_time = end_time)
					else:
						schedule_time_obj = ScheduleTime(manager_id = user_id, user_id = int(staff_id), start_date = start_date, end_date = end_date, start_time = start_time, end_time = end_time)
						schedule_time_obj.save()
						ScheduleTiming.objects.create(manager_id = user_id, user_id = int(staff_id), start_date = start_date, end_date = end_date, start_time = start_time, end_time = end_time, schedule_time_id = schedule_time_obj)
					# ScheduleTiming.objects.create(manager_id = user_id, user_id = int(staff_id), start_date = start_date, end_date = end_date, start_time = start_time, end_time = end_time)
					return HttpResponse(1)
			elif end_date < start_date:
				return HttpResponse("End date should not be less")
			else:
				# if start_time == end_time:
				# 	return HttpResponse("Time should not be same")
				# elif end_time < start_time:
				# 	return HttpResponse("End time should not be less")
				# else:
				delta = end_date - start_date

				schedule_time_obj = ScheduleTime.objects.filter(manager_id = user_id, user_id = int(staff_id),  start_date__year = start_time.year,  start_date__month  = start_time.month,  start_date__day  = start_time.day, end_date__year = end_time.year,  end_date__month  = end_time.month,  end_date__day  = end_time.day)
				if schedule_time_obj:
					schedule_time_obj_obj = schedule_time_obj.last()
				else:
					schedule_time_obj = ScheduleTime(manager_id = user_id, user_id = int(staff_id), start_date = start_date, end_date = end_date, start_time = start_time, end_time = end_time)
					schedule_time_obj.save()
					schedule_time_obj_obj = schedule_time_obj

				for i in range(delta.days + 1):
					day = start_date + timedelta(days=i)
					schedule_obj = ScheduleTiming.objects.filter(manager_id = user_id, user_id = int(staff_id),  start_date__year = day.year,  start_date__month  = day.month,  start_date__day  = day.day)
					if schedule_obj:
						schedule_obj.update(end_date = end_date, start_time = start_time, end_time = end_time)
					else:
						ScheduleTiming.objects.create(manager_id = user_id, user_id = int(staff_id), start_date = day, end_date = end_date, start_time = start_time, end_time = end_time, schedule_time_id_id = schedule_time_obj_obj.id)
				return HttpResponse(1)
		except Exception as f:
			print("-----------------",f)
			return HttpResponse(0)


@method_decorator(checkloginManager, name='dispatch')
class TaskList(TemplateView):
	template_name = "task-list.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		employee_id = kwargs["id"]
		# employee_id = self.request.GET.get('employee_id',None)
		manager_id = self.request.user.id
		if employee_id:

			user_tasks_obj = TaskModel.objects.filter(manager_id = manager_id, staff_user_id_id = int(employee_id)).order_by("created")
			context["task_count"] = user_tasks_obj.count()
			paginator = Paginator(user_tasks_obj, 25)
			page_number = self.request.GET.get('page')
			page_obj = paginator.get_page(page_number)
			context["page_obj"] = page_obj
		else:
			context["tasks"] = ""
		context["user_details"] = UserDetails.objects.get(user_id = int(employee_id))	
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
		context["timezones"] = all_timezones
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)
		return context


@method_decorator(checkloginManager, name='dispatch')
class AttendenceRecord(TemplateView):
	template_name = "attendance-record.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		user_id = kwargs["id"]
		manager_id = self.request.user.id
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
		context["timezones"] = all_timezones
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)
		context["user_details"] = UserDetails.objects.get(user_id = int(user_id))
		
		schedule_obj = ScheduleTiming.objects.filter(manager_id = manager_id, user_id = int(user_id))

		context["schedule_obj_count"] = schedule_obj.count()
		paginator = Paginator(schedule_obj, 25)
		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context["page_obj"] = page_obj
		return context


# @method_decorator(checkloginManager, name='dispatch')
class ManagerChatByUser(View):
	# template_name = "manager_chat_by_user.html"

	def post(self, request):

		print(request.POST)

		thread_id = request.POST.get("data_thread")
		thread_obj = ChatThread.objects.get(id = int(thread_id))

		manager_id = request.user.id

		context = {}
		if manager_id == thread_obj.sender.id:
			reciever_email = thread_obj.reciever.username
		else:
			reciever_email = thread_obj.sender.username


		ChatThread.objects.filter(sender_id = manager_id,reciever__username = reciever_email).update(archive = False)
		ChatThread.objects.filter(reciever__username = reciever_email,sender_id = manager_id).update(archive_2 = False)

		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)
		context["sender_timezone"] = context["manager_details"].timezone
		context["manager_id"] = context["manager_details"].manaager.id
		context["name"] = context["manager_details"].full_name
		context["reciever_email"] = request.user.username
		# chat_thread = ChatThread.objects.filter(sender_id = manager_id, archive = False, date_updated__isnull = False)
		# chat_thread_1 = ChatThread.objects.filter(reciever_id = manager_id, archive_2 = False, date_updated__isnull = False)

		# main_chat_thread = (chat_thread | chat_thread_1).order_by('-date_updated')


		try:
			UserType.objects.get(user__username = reciever_email)
			context["reciever_email"] = reciever_email
			reciever_div_id = reciever_email.replace(".","")
			context["reciever_div_id"] = reciever_div_id.replace("@","")
			user_div_id = (self.request.user.username).replace(".","")
			context["user_div_id"] = user_div_id.replace("@","")
			get_reciever_id = User.objects.get(username = reciever_email)
			context["reciever_id"] = get_reciever_id.id
			
			chat_messages = ChatMessage.objects.filter(thread_id = int(thread_id), thread__archive_2 = False, thread__archive = False)

			context["thread_id"] = thread_id



			# if chat_messages:
			# else:
			# 	cht_thread = ChatThread.objects.filter(sender_id = manager_id, reciever_id = get_reciever_id.id)
			# 	cht_thread_1 = ChatThread.objects.filter(sender_id = get_reciever_id.id, reciever_id = manager_id)
			# 	if cht_thread:
			# 		thead_obj = ChatThread.objects.filter(sender_id = manager_id, reciever_id = get_reciever_id.id)
			# 		thread_id = cht_thread[0].id
			# 	elif cht_thread_1:
			# 		thead_obj = ChatThread.objects.filter(sender_id = get_reciever_id.id, reciever_id = manager_id)
			# 		thread_id = cht_thread_1[0].id
			# 	else:
			# 		thead_obj = ChatThread.objects.create(sender_id = manager_id, reciever_id = get_reciever_id.id, archive = False, archive_2 = False)
			# 		thread_id = thead_obj.id
			# 		thead_obj = ChatThread.objects.filter(sender_id = manager_id, reciever_id = get_reciever_id.id)
			# 	context["thread_id"] = thread_id

			# 	if main_chat_thread:
			# 		main_chat_thread = (main_chat_thread | thead_obj).order_by('-date_updated')
			# 	else:
			# 		main_chat_thread = thead_obj

			# context["chat_thread"] = main_chat_thread

			user_obj = UserType.objects.get(user__username = reciever_email)
			if user_obj.normal_user:
				name_obj = UserDetails.objects.get(user__username = reciever_email)
				context["reciever_name"] = name_obj.name
				context["reciever_manager_id"] = name_obj.manager_id
				context["reciever_manager_timezone"] = name_obj.timezone
			elif user_obj.manager:
				name_obj = ManagerDetails.objects.get(manaager__username = reciever_email)
				context["reciever_name"] = name_obj.full_name
				context["reciever_manager_id"] = name_obj.manaager_id
				context["reciever_manager_timezone"] = name_obj.timezone

			if chat_messages:
				context['chat_messages'] = chat_messages
			else:
				context['chat_messages'] = ""
		except:
			context["user_does_not_exist"] = True
		posts_html = loader.render_to_string(
			'manager_chat_by_user.html',
			{'manager': context}
		)


		return HttpResponse(json.dumps(posts_html))


@method_decorator(checkloginManager, name='dispatch')
class ManagerChat(TemplateView):
	template_name = "manager_chat.html"

	def get_context_data(self, *args, **kwargs):
		context = {}


		manager_id = self.request.user.id
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
		context["timezones"] = all_timezones
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)


		chat_thread = ChatThread.objects.filter(sender_id = manager_id, archive = False, date_updated__isnull = False)
		chat_thread_1 = ChatThread.objects.filter(reciever_id = manager_id, archive_2 = False, date_updated__isnull = False)
		context["chat_thread"] = (chat_thread | chat_thread_1).order_by('-date_updated')
		context["reciever_email"] = self.request.user.username
		context["user_manager"] = True
		return context


class StaffProfileEdit(TemplateView):
	template_name = "staff_profile_edit.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		employee_id = int(kwargs['id'])

		manager_id = self.request.user.id
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
		context["timezones"] = all_timezones
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)

		user_details = UserDetails.objects.get(user_id = employee_id)
		try:
			context["user_details"]	= user_details
		except:
			context["user_details"]	= False
		context["departments"] = list(Departments.objects.all().values())
		context["employee_id"] = employee_id
		context["cities"] = Cities.objects.all()
		context["functions"] = Functions.objects.all()
		context["designations"] = Designation.objects.all()
		return context


class StaffProfileEditPost(View):
	def post(self, request):
		try:
			emergency_contact_person = request.POST.get("emergency_contact_person")
			staff_mem_email1 = request.POST.get("staff_mem_email1")
			department = request.POST.get("department")
			department_id = request.POST.get("department_id")
			user_id = int(request.POST.get("user_id"))

			email2 = request.POST.get("email2")
			email2 = email2.strip()
			phone1 = request.POST.get("phone1")
			phone1 = phone1.strip()
			phone2 = request.POST.get("phone2")
			phone2 = phone2.strip()
			password = request.POST.get("password")
			dummy_specification_line = request.POST.get("dummy_specification_line")
			dummy_specification_line = dummy_specification_line.strip()
			comment = request.POST.get("comment")
			comment = comment.strip()
			staff_timezone = request.POST.get("staff_timezone")
			staff_timezone = staff_timezone.strip()
			city = request.POST.get("city")
			city = city.strip()
			countdown_timer = request.POST.get("countdown_timer")
			function = request.POST.get("function")
			function = function.strip()
			designation = request.POST.get("designation")
			designation = designation.strip()
			user_obj = UserDetails.objects.get(user_id = user_id)
			check_user = User.objects.filter(username = staff_mem_email1)
			profile_pic = request.POST.get("profile_pic")



			if user_obj.user.username:
				user_obj.name = emergency_contact_person
				user_obj.save()

				imgdata = request.POST.get('profile_pic')
				if imgdata:
					image_name = str(int(time.time()))
					image = imgdata.split(";base64,")
					extens = image[0]
					ext = extens.split("/")
					extension = ext[1]
					base_image = image[1]
					b_image = base64.b64decode(base_image)
					filename = image_name + "." + extension
					
					image_path_to_saved = settings.PROFILE_IMAGE_PATH + filename
					file_path = settings.PROFILE_IMAGE_PATH + image_name

					with open(image_path_to_saved, 'wb') as f:
						f.write(b_image)

					profile_pic_model_path = image_path_to_saved.split("/static")
					# print(profile_pic_model_path)
					UserDetails.objects.filter(user_id = user_id).update(profile_pic = "/static"+profile_pic_model_path[-1])	

				UserDetails.objects.filter(user_id = user_id).update(phone_no_1 = phone1, department_id = int(department_id), function = function, designation = designation, count_timer = countdown_timer, city = city, timezone = staff_timezone, comment = comment, it_equipment_specification = dummy_specification_line, phone_no_2 = phone2, email2 = email2)
				
				user_obj = User.objects.get(id = user_id)
				user_obj.username = staff_mem_email1
				user_obj.email = staff_mem_email1
				user_obj.save()

				return HttpResponse(1)
			else:
				return HttpResponse(0)
		except Exception as y:
			print(y)
			return HttpResponse(0)


class GetChat(View):
	def get(self, request):
		thread_id = request.GET.get('chat_thread_id')
			
		try:
			manager_id = self.request.user.id
			thread_obj = ChatThread.objects.get(id = int(thread_id))
							
			try:
				try:					
					user_obj = ManagerDetails.objects.get(manaager_id = thread_obj.sender.id)
					if user_obj.manaager.id == manager_id:
						managerr_id = user_obj.manaager.id
					else:
						try:
							user_obj = ManagerDetails.objects.get(manaager_id = thread_obj.reciever.id)
							managerr_id = user_obj.manaager.id
						except:
							mng_obj = UserDetails.objects.get(user_id = thread_obj.reciever.id)
							managerr_id = mng_obj.user.id
				except:
					user_obj = ManagerDetails.objects.get(manaager_id = thread_obj.reciever.id)
					if user_obj.manaager.id == manager_id:
						managerr_id = user_obj.manaager.id
					else:
						try:
							user_obj = ManagerDetails.objects.get(manaager_id = thread_obj.sender.id)
							managerr_id = user_obj.manaager.id
						except:
							mng_obj = UserDetails.objects.get(user_id = thread_obj.sender.id)
							managerr_id = mng_obj.user.id
				
			except:
				try:
					user_obj = UserDetails.objects.get(user_id = thread_obj.sender.id)
					if user_obj.manager_id == manager_id:
						managerr_id = user_obj.user.id
					else:
						try:
							user_obj = UserDetails.objects.get(user_id = thread_obj.reciever.id)
							managerr_id = user_obj.user.id
						except:
							mng_obj = ManagerDetails.objects.get(manaager_id = thread_obj.reciever.id)
							managerr_id = mng_obj.manaager.id
				except:
					user_obj = UserDetails.objects.get(user_id = thread_obj.reciever.id)
					if user_obj.manager_id != manager_obj.manaager.id:
						managerr_id = user_obj.user.id
					else:
						try:
							user_obj = UserDetails.objects.get(user_id = thread_obj.sender.id)
							managerr_id = user_obj.user.id
						except:
							mng_obj = ManagerDetails.objects.get(manaager_id = thread_obj.sender.id)
							managerr_id = mng_obj.manaager.id


			messages_obj = ChatMessage.objects.annotate(
			    year=ExtractYear('created'),
			    month=ExtractMonth('created'),
			    day=ExtractDay('created'),
			    hour=ExtractHour('created'),
			    minute=ExtractMinute('created'),
			).values('sender_id','reciever_id','message','thread_id','year','month','day','hour','minute','name').filter(thread_id = int(thread_id))



			for i in list(messages_obj):
				print("sender_id", i["sender_id"])

			context = [{"messages_obj" : list(messages_obj), "managerr_id" : managerr_id}]

			return HttpResponse(json.dumps(context))
		except Exception as h:
			print("--------------------",h)
			return HttpResponse(0)


class GetSearchedUsersByManager(View):
	def post(self, request):
		try:

			manager_id = request.user.id
			search_query = request.POST.get('search_data')

			# employee_name_capital = search_query.capitalize()
			# employee_name_upper = search_query.upper()
			# employee_name_lower = search_query.lower()

			users = UserDetails.objects.filter(name__icontains = search_query, manager_id = manager_id).exclude(user_id = request.user.id)
			# users_capital = UserDetails.objects.filter(name__contains = employee_name_capital, manager_id = manager_id).exclude(user_id = request.user.id)
			# users_upper = UserDetails.objects.filter(name__contains = employee_name_upper, manager_id = manager_id).exclude(user_id = request.user.id)
			# users_lower = UserDetails.objects.filter(name__contains = employee_name_lower, manager_id = manager_id).exclude(user_id = request.user.id)

			# users = users | users_capital | users_upper |users_lower
			users = users

			# managers_name_capital = search_query.capitalize()
			# managers_name_upper = search_query.upper()
			# managers_name_lower = search_query.lower()

			managers = ManagerDetails.objects.filter(full_name__icontains = search_query , manaager_id = manager_id)
			# managers_capital = ManagerDetails.objects.filter(full_name__contains = managers_name_capital , manaager_id = manager_id)
			# managers_upper = ManagerDetails.objects.filter(full_name__contains = managers_name_upper , manaager_id = manager_id)
			# managers_lower = ManagerDetails.objects.filter(full_name__contains = managers_name_lower , manaager_id = manager_id)
			
			# managers = managers | managers_capital | managers_upper | managers_lower
			managers = managers

			final_users = list(users.values('name','user__username', 'user_id')) + list(managers.values('full_name','manaager__username','manaager_id'))
			return HttpResponse(json.dumps(final_users))
		except:
			return HttpResponse(0)


class GetChatByManager(View):
	def post(self, request):
		try:
			email = request.POST.get('email')
			sender_obj = ChatThread.objects.filter(sender_id = int(email), date_updated__isnull = False)
			receiver_obj = ChatThread.objects.filter(reciever_id = int(email), date_updated__isnull = False)
			manager_id = request.user.id

			final_obj = sender_obj | receiver_obj
			if final_obj:
				final_list = []
				for data in final_obj:
					context = {}
					sender_id = data.sender.id
					reciever_id = data.reciever.id
					try:
						try:
							manager_obj = ManagerDetails.objects.get(manaager_id = sender_id)
							if manager_obj.manaager.id == manager_id:
								name = manager_obj.full_name
								try:
									name_2_obj = ManagerDetails.objects.get(manaager_id = reciever_id)
									name_2 = name_2_obj.full_name
								except:
									name_2_obj = UserDetails.objects.get(user_id = reciever_id)
									name_2 = name_2_obj.name
							else:
								manager_obj = ManagerDetails.objects.get(manaager_id = reciever_id)
								name = manager_obj.full_name
								try:
									name_2_obj = ManagerDetails.objects.get(manaager_id = sender_id)
									name_2 = name_2_obj.full_name
								except:
									name_2_obj = UserDetails.objects.get(user_id = sender_id)
									name_2 = name_2_obj.name
						except:
							manager_obj = ManagerDetails.objects.get(manaager_id = reciever_id)
							if manager_obj.manaager.id == manager_id:
								name = manager_obj.full_name
								try:
									name_2_obj = ManagerDetails.objects.get(manaager_id = sender_id)
									name_2 = name_2_obj.full_name
								except:
									name_2_obj = UserDetails.objects.get(user_id = sender_id)
									name_2 = name_2_obj.name
							else:
								manager_obj = ManagerDetails.objects.get(manaager_id = sender_id)
								name = manager_obj.full_name
								try:
									name_2_obj = ManagerDetails.objects.get(manaager_id = reciever_id)
									name_2 = name_2_obj.full_name
								except:
									name_2_obj = UserDetails.objects.get(user_id = reciever_id)
									name_2 = name_2_obj.name
					except:
						try:
							manager_obj = UserDetails.objects.get(user_id = sender_id)
							if manager_obj.manager_id == manager_id:
								name = manager_obj.name
								try:
									name_2_obj = UserDetails.objects.get(user_id = reciever_id)
									name_2 = name_2_obj.name
								except:
									name_2_obj = ManagerDetails.objects.get(manaager_id = reciever_id)
									name_2 = name_2_obj.full_name
							else:
								manager_obj = UserDetails.objects.get(user_id = reciever_id)
								name = manager_obj.name
								try:
									name_2_obj = UserDetails.objects.get(user_id = sender_id)
									name_2 = name_2_obj.name
								except:
									name_2_obj = ManagerDetails.objects.get(manaager_id = sender_id)
									name_2 = name_2_obj.full_name
						except:
							manager_obj = UserDetails.objects.get(user_id = reciever_id)
							if manager_obj.manager_id == manager_id:
								name = manager_obj.name
								try:
									name_2_obj = UserDetails.objects.get(user_id = sender_id)
									name_2 = name_2_obj.name
								except:
									name_2_obj = ManagerDetails.objects.get(manaager_id = sender_id)
									name_2 = name_2_obj.full_name
							else:
								manager_obj = UserDetails.objects.get(user_id = sender_id)
								name = manager_obj.name
								try:
									name_2_obj = UserDetails.objects.get(user_id = reciever_id)
									name_2 = name_2_obj.name
								except:
									name_2_obj = ManagerDetails.objects.get(manaager_id = reciever_id)
									name_2 = name_2_obj.full_name
					
					last_msg_obj = ChatMessage.objects.filter(thread_id = data.id).last()

					context["name"] = name
					context["name2"] = name_2
					context["reciever_div_id_div"] = data.id
					context["chat_message"] = last_msg_obj.message

					date = str(data.date_updated)
					date_split = date.split(" ")
					date_split_ = (date_split[0]).split("-")
					date = date_split_[-1]+"/"+date_split_[1]+"/"+date_split_[0]

					time_split = date_split[1].split(":")
					ampm = "PM" if (int(time_split[0])) >= 12 else "AM"
					
					hours = (int(time_split[0])) % 12;
					hours = hours if hours >= 12 else time_split[0]

					context["date"] = date + " , "+ str(hours)+":"+time_split[1] + ":" + ampm
					final_list.append(context)
				return HttpResponse(json.dumps(final_list))
			else:
				return HttpResponse(5)
		except:
			return HttpResponse(0)


class OnlineManager(View):
	def post(self, request):
		try:
			manager_id = request.POST.get("user_id")
			user_obj = ManagerDetails.objects.get(manaager_id = int(manager_id))
			user_time = pytz.timezone(user_obj.timezone)
			user_time_ = datetime.now(user_time)
			user_time = user_time_.strftime('%Y-%m-%d %H:%M:%S')

			obj = OnlineStatusModel.objects.get(user_id = int(manager_id))
			obj.i_am_here = True
			obj.in_meeting = False
			obj.lunch_break = False
			obj.tea_break = False
			obj.offline = False
			obj.time = user_time
			obj.save()
			return HttpResponse(1)
		except:
			return HttpResponse(0)


class CronJobOnlineManager(View):
	def post(self,  request):
		try:
			print("---------------")
			managers = UserType.objects.filter(manager = True)

			for manager in managers:
				online_obj = OnlineStatusModel.objects.get(user_id = manager.user.id)
				if online_obj.i_am_here:
					user_obj = ManagerDetails.objects.get(manaager_id = manager.user.id)
					user_time = pytz.timezone(user_obj.timezone)
					user_time_ = datetime.now(user_time)
					last_time = online_obj.time
					user_time_ = parse(user_time_.strftime('%Y-%m-%d %H:%M:%S'))
					if user_time_.date() == last_time.date():
						user_time_hour = (user_time_.hour * 60) + user_time_.minute + (user_time_.second/60)
						last_time_hour = (last_time.hour * 60) + last_time.minute + (last_time.second/60)
						final_minutes = user_time_hour - last_time_hour
					else:
						time_fifference = user_time_.replace(tzinfo=None) - last_time.replace(tzinfo=None)
						final_minutes = (time_fifference.total_seconds())/60
					if final_minutes > 5:
						time = user_time_.strftime('%Y-%m-%d %H:%M:%S')
						online_obj.i_am_here = False
						online_obj.in_meeting = False
						online_obj.lunch_break = False
						online_obj.tea_break = False
						online_obj.offline = True
						online_obj.time = time
						online_obj.save()
						status = "offline"

						status_ws = create_connection(socket_url+"/chat_bxx/")
						staff_div_id = online_obj.user.username
						staff_div_id = staff_div_id.replace(".", "")
						staff_div_id = staff_div_id.replace("@", "")
						status_ws.send(json.dumps({"status" : status, "staff_div_id" : staff_div_id}))
						sleep(4)
						status_ws.close()


			staff_users = UserType.objects.filter(normal_user = True)
			for user in staff_users:
				online_obj = OnlineStatusModel.objects.get(user_id = user.user.id)
				user_obj = UserDetails.objects.get(user_id = online_obj.user.id)
				user_time = pytz.timezone(user_obj.timezone)
				user_time_ = datetime.now(user_time)
				last_time = online_obj.time
				if online_obj.offline:
					pass
				else:
					user_time_ = parse(user_time_.strftime('%Y-%m-%d %H:%M:%S'))
					
					if user_time_.date() == last_time.date():
						user_time_hour = (user_time_.hour * 60) + user_time_.minute + (user_time_.second/60)
						last_time_hour = (last_time.hour * 60) + last_time.minute + (last_time.second/60)
						final_minutes = user_time_hour - last_time_hour
					else:
						# print(user_time_.replace(tzinfo=None))
						# print(last_time.replace(tzinfo=None))
						# print("here-----------")
						# naive = dt.replace(tzinfo=None)
						time_fifference = user_time_.replace(tzinfo=None) - last_time.replace(tzinfo=None)
						final_minutes = (time_fifference.total_seconds())/60
					if final_minutes > 3:
						online_obj.i_am_here = False
						online_obj.in_meeting = False
						online_obj.lunch_break = False
						online_obj.tea_break = False
						online_obj.offline = True
						online_obj.time = user_time_
						online_obj.save()
						# user_obj.last_countdown_timer_time = user_time_
						# user_obj.save()
						status = "offline"

						manager_id_obj = UserDetails.objects.get(user_id = online_obj.user.id)
						manager_obj = User.objects.get(id = manager_id_obj.manager_id)
						url = socket_url + "/manager_notify/"+str(manager_obj.username)+"/"
						ws = create_connection(url)

						ws.send(json.dumps({'user_id': int(manager_obj.id), "status" : status, "staff_id" : online_obj.user.id}))


						status_ws = create_connection(socket_url+"/chat_bxx/")
						staff_div_id = online_obj.user.username
						staff_div_id = staff_div_id.replace(".", "")
						staff_div_id = staff_div_id.replace("@", "")
						status_ws.send(json.dumps({"status" : status, "staff_div_id" : staff_div_id}))

						sleep(5)
						ws.close()
						status_ws.close()

			return HttpResponse(1)
		except Exception as g:
			print(g)
			return HttpResponse(0)


class NewChatThread(View):
	def post(self, request):
		try:
			context = {}
			usermname = request.POST.get("email")
			user_id = int(request.POST.get("user_id"))

			user_obj = UserType.objects.get(user_id = user_id)
			if user_obj.normal_user:
				# User.objects.get(id = user_id)
				context["user_manager"] = False
			else:
				context["user_manager"] = True


			chat_thread_1 = ChatThread.objects.filter(sender_id = user_id, reciever__username = usermname)
			if not chat_thread_1:
				chat_thread_1 = ChatThread.objects.filter(sender__username= usermname, reciever_id = user_id)

			if not chat_thread_1:
				user_obj = User.objects.get(username = usermname)
				chat_thread_obj = ChatThread(sender_id = user_id, reciever_id = user_obj.id)
				chat_thread_obj.save()
			else:
				chat_thread_obj = chat_thread_1[0]


			last_message = ChatMessage.objects.filter(thread_id = chat_thread_obj.id).last()
			try:
				context["last_message"] = last_message.message
			except:
				context["last_message"] = ""

			if chat_thread_obj.sender.id == user_id:

				last_updated = chat_thread_obj.date_updated
				username = chat_thread_obj.reciever.username
				context["reciever_email"] = username
				username = username.replace("@", "")
				username = username.replace(".", "")
				context["reciever_email_id"] = username 
			else:
				last_updated = chat_thread_obj.date_updated_receiver
				username = chat_thread_obj.sender.username
				context["reciever_email"] = username
				username = username.replace("@", "")
				username = username.replace(".", "")
				context["reciever_email_id"] = username


			if last_updated:
				context["last_updated"] = last_updated
			else:
				context["last_updated"] = ""

			user_obj = UserType.objects.get(user__username = context["reciever_email"])
			if user_obj.normal_user:
				name_obj = UserDetails.objects.get(user__username = context["reciever_email"])
				context["reciever_name"] = name_obj.name
				
			elif user_obj.manager:
				name_obj = ManagerDetails.objects.get(manaager__username = context["reciever_email"])
				context["reciever_name"] = name_obj.full_name
				
			
			online_status = OnlineStatusModel.objects.get(user__username = context["reciever_email"])

			if online_status.i_am_here:
				icon_class = "green"
			elif online_status.in_meeting:
				icon_class = "orange"
			elif online_status.lunch_break:
				icon_class = "orange"
			elif online_status.tea_break:
				icon_class = "orange"
			else:
				icon_class = "red"
			context["icon_class"] = icon_class
			context["chat_id"] = chat_thread_obj.id



			posts_html = loader.render_to_string(
				'chat_thread_append.html',
				{'manager': context}
			)


			return HttpResponse(json.dumps(posts_html))
		except Exception as y:
			print(y)
			return HttpResponse(1)


@method_decorator(checkloginManager, name='dispatch')
class IndividualStaffResource(TemplateView):
	template_name = "individual_staff_resource.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		try:
			search_name = self.request.GET.get('search_name', None)
			employee_id = kwargs["id"]
			context["user_details"]	= UserDetails.objects.get(user_id = employee_id)

			if search_name:
				context["assigned_resources"] = AssignedDepartments.objects.filter(departments_id = context["user_details"].department.id, name__icontains = search_name)
			else:
				context["assigned_resources"] = AssignedDepartments.objects.filter(departments_id = context["user_details"].department.id)

			manager_id = self.request.user.id
			context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
			context["timezones"] = all_timezones
			context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)

			context["employee_id"] = employee_id
		except:
			pass
		
		return context


def meeting(request, meeting_id):
    # user = request.user
    # companyuser = CompanyUsers.objects.get(user=user)
    context = {}
    try:
    	name_obj = ManagerDetails.objects.get(manaager_id = request.user.id)
    	name = name_obj.full_name
    except:
    	name_obj = UserDetails.objects.get(user_id = request.user.id)
    	name = name_obj.name

    return render(request, "meeting.html", {'mid' : meeting_id, 'name': name}) 


class ReportingModule(TemplateView):
	template_name = "reporting_module.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		user_id = kwargs["id"]
		manager_id = self.request.user.id
		context["user_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
		context["timezones"] = all_timezones
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)
		context["user_details"] = UserDetails.objects.get(user_id = int(user_id))
		
		schedule_obj = ScheduleTiming.objects.filter(manager_id = manager_id, user_id = int(user_id))

		context["schedule_obj_count"] = schedule_obj.count()
		paginator = Paginator(schedule_obj, 25)
		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context["page_obj"] = page_obj
		return context






# Admin section
@method_decorator(checkloginSuperuser, name='dispatch')
class AdminDashboard(TemplateView):
	template_name = "Master-admin.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		context["managers"] = ManagerDetails.objects.all().order_by("-id")[0:10]
		context["managers_count"] = ManagerDetails.objects.all().count()
		return context


class AddDepartment(View):
	def post(self, request):
		department_name = (request.POST.get("department_name")).strip()
		department_obj = Departments.objects.filter(departments = department_name)
		if department_obj:
			return HttpResponse("Already exist")
		else:
			Departments.objects.create(departments = department_name)
			return HttpResponse("department created")


class AddCity(View):
	def post(self, request):
		city_name = (request.POST.get("city_name")).strip()
		cities_obj = Cities.objects.filter(cities = city_name)
		if cities_obj:
			return HttpResponse("Already exist")
		else:
			Cities.objects.create(cities = city_name)
			return HttpResponse("City created")


class Addfunction(View):
	def post(self, request):
		function_name = (request.POST.get("function_name")).strip()
		function_obj = Functions.objects.filter(function = function_name)
		if function_obj:
			return HttpResponse("Already exist")
		else:
			Functions.objects.create(function = function_name)
			return HttpResponse("Function created")


class AddDesignation(View):
	def post(self, request):
		designation_name = (request.POST.get("designation_name")).strip()
		designation_obj = Designation.objects.filter(designation = designation_name)
		if designation_obj:
			return HttpResponse("Already exist")
		else:
			Designation.objects.create(designation = designation_name)
			return HttpResponse("Designation created")


@method_decorator(checkloginSuperuser, name='dispatch')
class AddManager(TemplateView):
	template_name = "add_manager.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		user_id = self.request.user.id
		context["departments"] = list(Departments.objects.all().values())
		context["designations"] = Designation.objects.all()
		context["timezones"] = all_timezones

		return context


	def post(self, request):
		try:
			full_name = request.POST.get("emergency_contact_person")
			email = request.POST.get("email")
			contact_number = request.POST.get("contact_number")
			timezone1 = request.POST.get("timezone1")
			timezone2 = request.POST.get("timezone2")
			timezone3 = request.POST.get("timezone3")
			timezone4 = request.POST.get("timezone4")
			department = request.POST.get("department")
			department_id = request.POST.get("department_id")
			designation = request.POST.get("designation")
			password = request.POST.get("password")
			manager_timezone = request.POST.get('manager_timezone')
			user_obj = User.objects.filter(username = email)
			if user_obj:
				return HttpResponse("already exists")
			else:	
				user = User.objects.create(username = email, email = email, is_superuser = False)
				user.set_password(password)
				user.save()

				ManagerDetails.objects.create(manaager_id = user.id, department_id = int(department_id), designation = (designation), phone = contact_number, full_name = full_name, timezone = manager_timezone)
				InvalidAttempts.objects.create(user_id = user.id, attempts = 0, blocked = False)
				ManagerTimezones.objects.create(manager_id = user.id, timezone1 = timezone1, timezone2 = timezone2, timezone3 = timezone3, timezone4 = timezone4)
				UserType.objects.create(user_id = user.id,manager = True, normal_user = False)
				OnlineStatusModel.objects.create(user_id = user.id, i_am_here = False, in_meeting = False, lunch_break = False, tea_break = False, offline = True, time = timezone.now())
				return HttpResponse("User Created")
		except Exception as a:
			print(a)
			return HttpResponse("Issue occur")


class ChangeManagerPassword(View):
	def post(self, request):
		try:
			email = request.POST.get("email")
			new_pass = request.POST.get("password")
			user_obj = User.objects.get(username = email)
			user_obj.set_password(new_pass)
			user_obj.save()
			return HttpResponse(1)
		except Exception as f:
			print(f)
			return HttpResponse(0)


class CheckUserOnlineStatus(View):
	def post(self, request):
		try:
			user_id = request.POST.get('user_id')
			time = timezone.now()
			user_obj = OnlineStatusModel.objects.filter(user_id = user_id).last()
			if user_obj:
				subtract_time = time - user_obj.time
				# if user_obj.i_am_here:
				# 	if subtract_time.total_seconds() > 300:
				# 		OnlineStatusModel.objects.filter(user_id = user_id).update(offline = True, i_am_here = False, in_meeting = False, lunch_break = False, tea_break = False, time = time.now())
				# else:
				# 	OnlineStatusModel.objects.filter(user_id = user_id).update(offline = True, i_am_here = False, in_meeting = False, lunch_break = False, tea_break = False, time = time.now())
			response = list(OnlineStatusModel.objects.filter(user_id = user_id).values('user_id', 'user__username', 'offline', 'i_am_here', 'in_meeting', 'lunch_break', 'tea_break'))
			return HttpResponse(json.dumps(response))
		except:
			pass	
		return HttpResponse(1)


@method_decorator(checkloginSuperuser, name='dispatch')
class ManagerList(TemplateView):
	template_name = "manager_list.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		maanger_name = self.request.GET.get("maanger_name", None)
		if maanger_name:
			maanger_name_capital = maanger_name.capitalize()
			maanger_name_upper = maanger_name.upper()
			maanger_name_lower = maanger_name.lower()

			user_managers_obj =  ManagerDetails.objects.filter(Q(full_name__icontains = maanger_name) | Q(department__departments__icontains = maanger_name) | Q(designation__icontains = maanger_name) | Q(timezone__icontains = maanger_name)).order_by("-id")

			


			# user_managers_obj_capital =  ManagerDetails.objects.filter(Q(full_name__contains = maanger_name_capital) | Q(department__departments__contains = maanger_name_capital) | Q(designation__contains = maanger_name_capital) | Q(timezone__contains = maanger_name_capital)).order_by("-id")

			# user_managers_obj_upper =  ManagerDetails.objects.filter(Q(full_name__contains = maanger_name_upper) | Q(department__departments__contains = maanger_name_upper) | Q(designation__contains = maanger_name_upper) | Q(timezone__contains = maanger_name_upper)).order_by("-id")

			# user_managers_obj_lower =  ManagerDetails.objects.filter(Q(full_name__contains = maanger_name_lower) | Q(department__departments__contains = maanger_name_lower) | Q(designation__contains = maanger_name_lower) | Q(timezone__contains = maanger_name_lower)).order_by("-id")
			
			user_managers_obj = user_managers_obj
			context["manager_name"] = maanger_name
		else:
			user_managers_obj = ManagerDetails.objects.all().order_by("-id")
		context["managers_count"] = user_managers_obj.count()
		paginator = Paginator(user_managers_obj, 25)
		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context["page_obj"] = page_obj
		return context


@method_decorator(checkloginSuperuser, name='dispatch')
class ManagerProfileEdit(TemplateView):
	template_name = "manager_profile_edit.html"

	def get_context_data(self, *args, **kwargs):
		context = {}
		manager_id = int(kwargs["id"])
		context["manager_details"] = ManagerDetails.objects.get(manaager_id = manager_id)
		context["departments"] = Departments.objects.all()
		context["manager_id"] = manager_id
		context["timezones"] = all_timezones
		context["manager_timezones"] = ManagerTimezones.objects.get(manager_id = manager_id)
		context["designations"] = Designation.objects.all()
		return context



class ManagerProfileEditPost(View):
	def post(self, request):
		try:
			print(request.POST)
			emergency_contact_person = request.POST.get('emergency_contact_person')
			email = request.POST.get('email')
			email = email.strip()
			department = request.POST.get('department')
			department = department.strip()
			department_id = request.POST.get('department_id')
			manager_id = int(request.POST.get('manager_id'))
			contact_number = request.POST.get('contact_number')
			contact_number = contact_number.strip()
			timezone1 = request.POST.get('timezone1')
			timezone1 = timezone1.strip()
			timezone2 = request.POST.get('timezone2')
			timezone2 = timezone2.strip()
			timezone3 = request.POST.get('timezone3')
			timezone3 = timezone3.strip()
			timezone4 = request.POST.get('timezone4')
			timezone4 = timezone4.strip()
			department = request.POST.get('department')
			designation = request.POST.get('designation')
			designation = designation.strip()
			manager_timezone = request.POST.get('manager_timezone')
			manager_timezone = manager_timezone.strip()
			# return HttpResponse(1)
			manager_obj = ManagerDetails.objects.get(manaager_id = manager_id)			
			check_user = User.objects.filter(username = email)
			if manager_obj.manaager.username:

				ManagerTimezones.objects.filter(manager_id = manager_id).update(timezone1 = timezone1, timezone2 = timezone2, timezone3 = timezone3, timezone4 = timezone4)

				manager_obj.full_name = emergency_contact_person
				manager_obj.phone = contact_number
				manager_obj.designation = designation
				manager_obj.timezone = manager_timezone
				manager_obj.save()

				ManagerDetails.objects.filter(manaager_id = manager_id).update(department_id = int(department_id))
				
				user_obj = User.objects.get(id = manager_id)
				user_obj.username = email
				user_obj.email = email
				user_obj.save()
				return HttpResponse(1)
			# else:
			# 	if check_user:
			# 		return HttpResponse(5)
			# 	else:
			# 		manager_obj.full_name = emergency_contact_person
			# 		manager_obj.save()

			# 		ManagerDetails.objects.filter(manaager_id = manager_id).update(department_id = int(department_id))
					
			# 		user_obj = User.objects.get(id = manager_id)
			# 		user_obj.username = email
			# 		user_obj.email = email
			# 		user_obj.save()
			# 		return HttpResponse(1)
		except Exception as h:
			print(h)
			return HttpResponse(0)