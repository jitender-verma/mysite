-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: screenmonitor
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add departments',7,'add_departments'),(26,'Can change departments',7,'change_departments'),(27,'Can delete departments',7,'delete_departments'),(28,'Can view departments',7,'view_departments'),(29,'Can add manager timezones',8,'add_managertimezones'),(30,'Can change manager timezones',8,'change_managertimezones'),(31,'Can delete manager timezones',8,'delete_managertimezones'),(32,'Can view manager timezones',8,'view_managertimezones'),(33,'Can add user type',9,'add_usertype'),(34,'Can change user type',9,'change_usertype'),(35,'Can delete user type',9,'delete_usertype'),(36,'Can view user type',9,'view_usertype'),(37,'Can add user details',10,'add_userdetails'),(38,'Can change user details',10,'change_userdetails'),(39,'Can delete user details',10,'delete_userdetails'),(40,'Can view user details',10,'view_userdetails'),(41,'Can add task model',11,'add_taskmodel'),(42,'Can change task model',11,'change_taskmodel'),(43,'Can delete task model',11,'delete_taskmodel'),(44,'Can view task model',11,'view_taskmodel'),(45,'Can add staff status model',12,'add_staffstatusmodel'),(46,'Can change staff status model',12,'change_staffstatusmodel'),(47,'Can delete staff status model',12,'delete_staffstatusmodel'),(48,'Can view staff status model',12,'view_staffstatusmodel'),(49,'Can add saved document model',13,'add_saveddocumentmodel'),(50,'Can change saved document model',13,'change_saveddocumentmodel'),(51,'Can delete saved document model',13,'delete_saveddocumentmodel'),(52,'Can view saved document model',13,'view_saveddocumentmodel'),(53,'Can add invalid attempts',14,'add_invalidattempts'),(54,'Can change invalid attempts',14,'change_invalidattempts'),(55,'Can delete invalid attempts',14,'delete_invalidattempts'),(56,'Can view invalid attempts',14,'view_invalidattempts'),(57,'Can add email model',15,'add_emailmodel'),(58,'Can change email model',15,'change_emailmodel'),(59,'Can delete email model',15,'delete_emailmodel'),(60,'Can view email model',15,'view_emailmodel'),(61,'Can add comments model',16,'add_commentsmodel'),(62,'Can change comments model',16,'change_commentsmodel'),(63,'Can delete comments model',16,'delete_commentsmodel'),(64,'Can view comments model',16,'view_commentsmodel'),(65,'Can add assigned departments',17,'add_assigneddepartments'),(66,'Can change assigned departments',17,'change_assigneddepartments'),(67,'Can delete assigned departments',17,'delete_assigneddepartments'),(68,'Can view assigned departments',17,'view_assigneddepartments'),(69,'Can add alert model',18,'add_alertmodel'),(70,'Can change alert model',18,'change_alertmodel'),(71,'Can delete alert model',18,'delete_alertmodel'),(72,'Can view alert model',18,'view_alertmodel'),(73,'Can add captcha store',19,'add_captchastore'),(74,'Can change captcha store',19,'change_captchastore'),(75,'Can delete captcha store',19,'delete_captchastore'),(76,'Can view captcha store',19,'view_captchastore'),(77,'Can add manager details',20,'add_managerdetails'),(78,'Can change manager details',20,'change_managerdetails'),(79,'Can delete manager details',20,'delete_managerdetails'),(80,'Can view manager details',20,'view_managerdetails'),(81,'Can add cities',21,'add_cities'),(82,'Can change cities',21,'change_cities'),(83,'Can delete cities',21,'delete_cities'),(84,'Can view cities',21,'view_cities');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$C9yteQE79rNY$3jFhvVN8mHNqfA8JWCF9oKiRbNfDGD3wfRme2/jwcLo=','2020-05-29 09:01:58.679058',1,'root@root.com','','','root@root.com',1,1,'2020-05-25 13:19:46.000000'),(2,'pbkdf2_sha256$180000$v1WJuVl20gf3$QUD1yV2XkaUQg+MZsuxzOXwJujmEp4WjhnlbKVTZ/GI=','2020-06-01 05:42:48.092232',0,'example@example.com','jatin','','example@example.com',0,1,'2020-05-25 13:23:22.000000'),(3,'pbkdf2_sha256$180000$phJDIyfCNaPb$GwOnMh8ebkk9APjGId232m8x7zuZBg1WEn/0uG8CoBs=','2020-05-29 12:14:01.429998',0,'admin@manager.com','','','admin@manager.com',0,1,'2020-05-25 13:24:24.000000'),(5,'pbkdf2_sha256$180000$YFttCwnnV7J7$2KAjfvv99Z17tbUANTKiy4e5e9sjifaTMXpf0/bZAsY=','2020-05-26 07:24:32.319660',0,'test@abc.com','','','test@abc.com',0,1,'2020-05-26 07:23:33.721512'),(8,'pbkdf2_sha256$180000$iVceyUI79Se5$yPrFkLeknhCiAw65TkHDOcuT8NMy6Wz4coRhEMiBqAI=','2020-05-27 06:37:47.037878',1,'root','','','',1,1,'2020-05-27 06:37:28.912433'),(10,'pbkdf2_sha256$180000$MkJI1Al0D7Uv$EWogxMzldyIKgCg8l1WjJo6AFS2VbX4lBvIirpEIp5U=',NULL,0,'jitender@visions.net.in','','','jitender@visions.net.in',0,1,'2020-05-27 06:41:57.528300'),(11,'pbkdf2_sha256$180000$cGVwc5Uwun7j$pEM9VEWxs74zuswkXBVPL5FUhk4V8JvL7eqHAAaNxjM=','2020-05-27 13:18:55.879554',0,'testemp@gmail.com','','','testemp@gmail.com',0,1,'2020-05-27 13:11:53.092893'),(13,'pbkdf2_sha256$180000$QGitkjy91YY4$6n5VP3mAArkGe+tgxX1AhXvDlef5A79C/vCfitHT32Q=','2020-05-29 04:55:02.370399',0,'manu@manu.manu','','','manu@manu.manu',0,1,'2020-05-29 04:35:44.890222'),(14,'pbkdf2_sha256$180000$CKRQzZDWdrVM$EFkpWA54FAS7vC7AlnRWJJhoA0qzKteWGrIaiw7u02w=','2020-05-29 04:47:16.884880',0,'tarun@tarun.tarun','','','tarun@tarun.tarun',0,1,'2020-05-29 04:42:51.657251'),(18,'pbkdf2_sha256$180000$IQwWQ9Se7Yrz$PQmIJBndeH74CsFX/lzYyVtl5E23Ef0vfeChBs09tPg=',NULL,0,'ads@ccc.cc','','','ads@ccc.cc',0,1,'2020-05-29 05:24:20.046993'),(19,'pbkdf2_sha256$180000$7eW1YqTitrNh$8AHifI9WjD3lz23Ny6xi9KpDqwri+65k+KjgTzT3zeg=',NULL,0,'sam1@gmail.com','','','sam1@gmail.com',0,1,'2020-06-01 04:44:37.900561'),(20,'pbkdf2_sha256$180000$EUr7GPgIxrLm$JZ0K3w/FY6gelFUpuZ1b2HE/PGxoncmeTTAUUAjnaxs=',NULL,0,'sam@gmail.com','','','sam@gmail.com',0,1,'2020-06-01 04:57:42.454743'),(21,'pbkdf2_sha256$180000$2q7Rc3KYIWD3$iYaLAxqxrd34Jqktpq1Yq48UhBOOg6doAymAGKVp/mQ=',NULL,0,'sam@12gmail.com','','','sam@12gmail.com',0,1,'2020-06-01 05:10:55.475838');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `captcha_captchastore`
--

DROP TABLE IF EXISTS `captcha_captchastore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `captcha_captchastore`
--

LOCK TABLES `captcha_captchastore` WRITE;
/*!40000 ALTER TABLE `captcha_captchastore` DISABLE KEYS */;
/*!40000 ALTER TABLE `captcha_captchastore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-05-25 13:21:51.971361','1','dept_1',1,'[{\"added\": {}}]',7,1),(2,'2020-05-25 13:22:05.516176','2','dept_2',1,'[{\"added\": {}}]',7,1),(3,'2020-05-25 13:22:12.276933','3','dept_3',1,'[{\"added\": {}}]',7,1),(4,'2020-05-25 13:23:22.667971','2','example@example.com',1,'[{\"added\": {}}]',4,1),(5,'2020-05-25 13:24:04.448567','2','example@example.com',2,'[{\"changed\": {\"fields\": [\"First name\", \"Email address\"]}}]',4,1),(6,'2020-05-25 13:24:24.868071','3','admin@manager.com',1,'[{\"added\": {}}]',4,1),(7,'2020-05-25 13:24:52.062645','3','admin@manager.com',2,'[{\"changed\": {\"fields\": [\"Email address\"]}}]',4,1),(8,'2020-05-25 13:26:04.972807','1','example@example.com',1,'[{\"added\": {}}]',10,1),(9,'2020-05-25 13:26:34.859817','1','example@example.com',1,'[{\"added\": {}}]',9,1),(10,'2020-05-25 13:26:45.607523','2','admin@manager.com',1,'[{\"added\": {}}]',9,1),(11,'2020-05-25 13:27:27.410088','1','admin@manager.com',1,'[{\"added\": {}}]',14,1),(12,'2020-05-25 13:27:38.461637','2','example@example.com',1,'[{\"added\": {}}]',14,1),(13,'2020-05-25 13:28:46.766416','1','example@example.com',1,'[{\"added\": {}}]',18,1),(14,'2020-05-26 06:22:52.400976','3','root',1,'[{\"added\": {}}]',14,1),(15,'2020-05-26 06:23:24.513150','1','root@root.com',2,'[{\"changed\": {\"fields\": [\"Username\", \"Email address\"]}}]',4,1),(16,'2020-05-26 06:27:21.569863','3','root@root.com',2,'[{\"changed\": {\"fields\": [\"Attempts\"]}}]',14,1),(17,'2020-05-26 06:42:05.996642','1','3',1,'[{\"added\": {}}]',8,1),(18,'2020-05-26 07:28:09.949611','2','test@abc.com',1,'[{\"added\": {}}]',18,1),(19,'2020-05-26 09:17:34.729217','1','dept_1',3,'',17,1),(20,'2020-05-26 09:18:24.532220','1','admin@manager.com',3,'',13,1),(21,'2020-05-27 06:38:16.447297','6','jitender@visions.net.in',3,'',4,8),(22,'2020-05-27 06:41:51.750117','9','jitender@visions.net.in',3,'',4,8),(23,'2020-05-29 05:08:46.100167','4','tarun@tarun.tarun',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',10,1),(24,'2020-05-29 05:22:48.244668','7','ads@ccc.cc',3,'',10,1),(25,'2020-05-29 05:22:48.285032','6','asd@asdasdasd.asda',3,'',10,1),(26,'2020-05-29 05:22:48.320492','5','esfera@asd.asd',3,'',10,1),(27,'2020-05-29 05:22:48.434861','4','tarun@tarun.tarun',3,'',10,1),(28,'2020-05-29 05:24:09.559683','17','ads@ccc.cc',3,'',4,1),(29,'2020-05-29 05:24:09.601436','16','asd@asdasdasd.asda',3,'',4,1),(30,'2020-05-29 05:24:09.634680','4','bakasur@abc.com',3,'',4,1),(31,'2020-05-29 05:24:09.751506','15','esfera@asd.asd',3,'',4,1),(32,'2020-05-29 05:24:09.785251','12','vv@vv.vom',3,'',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(19,'captcha','captchastore'),(5,'contenttypes','contenttype'),(18,'normal_user','alertmodel'),(17,'normal_user','assigneddepartments'),(21,'normal_user','cities'),(16,'normal_user','commentsmodel'),(7,'normal_user','departments'),(15,'normal_user','emailmodel'),(14,'normal_user','invalidattempts'),(20,'normal_user','managerdetails'),(8,'normal_user','managertimezones'),(13,'normal_user','saveddocumentmodel'),(12,'normal_user','staffstatusmodel'),(11,'normal_user','taskmodel'),(10,'normal_user','userdetails'),(9,'normal_user','usertype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-05-25 13:17:05.219188'),(2,'auth','0001_initial','2020-05-25 13:17:07.797706'),(3,'admin','0001_initial','2020-05-25 13:17:16.211956'),(4,'admin','0002_logentry_remove_auto_add','2020-05-25 13:17:18.229334'),(5,'admin','0003_logentry_add_action_flag_choices','2020-05-25 13:17:18.282487'),(6,'contenttypes','0002_remove_content_type_name','2020-05-25 13:17:19.843955'),(7,'auth','0002_alter_permission_name_max_length','2020-05-25 13:17:20.011406'),(8,'auth','0003_alter_user_email_max_length','2020-05-25 13:17:20.145488'),(9,'auth','0004_alter_user_username_opts','2020-05-25 13:17:20.197407'),(10,'auth','0005_alter_user_last_login_null','2020-05-25 13:17:20.922122'),(11,'auth','0006_require_contenttypes_0002','2020-05-25 13:17:20.989275'),(12,'auth','0007_alter_validators_add_error_messages','2020-05-25 13:17:21.041718'),(13,'auth','0008_alter_user_username_max_length','2020-05-25 13:17:21.215321'),(14,'auth','0009_alter_user_last_name_max_length','2020-05-25 13:17:21.357408'),(15,'auth','0010_alter_group_name_max_length','2020-05-25 13:17:21.549507'),(16,'auth','0011_update_proxy_permissions','2020-05-25 13:17:21.655601'),(17,'captcha','0001_initial','2020-05-25 13:17:22.062928'),(18,'normal_user','0001_initial','2020-05-25 13:17:26.481456'),(19,'sessions','0001_initial','2020-05-25 13:17:38.613930'),(20,'normal_user','0002_managerdetails','2020-05-26 13:29:07.979268'),(21,'normal_user','0003_managerdetails_phone','2020-05-27 06:26:38.747946'),(22,'normal_user','0004_auto_20200528_1125','2020-05-28 11:25:47.130789'),(23,'normal_user','0005_cities','2020-05-29 08:45:27.637053');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3zd06ry0eqvscj4i6gg9amejlsjw12w8','ZmM4NzBjMDMxOTFlYWM0MjIwNDI3NmJmZmM2YTE0MDY4NmMwMzBiNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1YjY4YWM2MGQwYTgzZDc3ZDczMTVjZDNlODE2ZWEyZmRiYmEzY2M1In0=','2020-06-08 13:21:39.628580'),('ea7izps4n6wjb5cfa7xlf02r20jspfun','ZmM4NzBjMDMxOTFlYWM0MjIwNDI3NmJmZmM2YTE0MDY4NmMwMzBiNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1YjY4YWM2MGQwYTgzZDc3ZDczMTVjZDNlODE2ZWEyZmRiYmEzY2M1In0=','2020-06-09 06:22:05.551575'),('oj56c6ndkkvlbtgfbzp30zeroj8vmpfa','YTE2ZTlkM2QxYTY1YTMwYzUwNmZmMWM4MGZmMGViOWFlMzEwOWQyYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMjAzMTc1MzIyYWExM2Q1NDhlNGYyNmZjNWI2OGQ5Yjg5NjIwNmI4In0=','2020-06-15 05:42:48.133715'),('wj81t3mouuyn0fnx5k64yq4pjj59tlu9','ZGU0ZTk2NTZkOTdiMDYyNDIyYzk4NzJjZmM0YzAwNWI1YjI1YzhmNTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMmNiY2FlNjRmNjlmM2ZhMmM3ODA3ZjFiZTNkZTlhMDgwZDRmMDMyIn0=','2020-06-12 12:14:01.512329');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_alertmodel`
--

DROP TABLE IF EXISTS `normal_user_alertmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_alertmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` int(11) DEFAULT NULL,
  `alert` tinyint(1) NOT NULL,
  `staff_user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_alertmodel_staff_user_id_id_bb3b23ff_fk_auth_user_id` (`staff_user_id_id`),
  CONSTRAINT `normal_user_alertmodel_staff_user_id_id_bb3b23ff_fk_auth_user_id` FOREIGN KEY (`staff_user_id_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_alertmodel`
--

LOCK TABLES `normal_user_alertmodel` WRITE;
/*!40000 ALTER TABLE `normal_user_alertmodel` DISABLE KEYS */;
INSERT INTO `normal_user_alertmodel` VALUES (1,3,1,2),(2,3,0,5),(3,3,0,11),(4,13,0,14),(5,13,0,18),(6,3,0,19),(7,3,0,20),(8,3,0,21);
/*!40000 ALTER TABLE `normal_user_alertmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_assigneddepartments`
--

DROP TABLE IF EXISTS `normal_user_assigneddepartments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_assigneddepartments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `path` longtext,
  `departments_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_assigned_departments_id_4a934b7f_fk_normal_us` (`departments_id`),
  CONSTRAINT `normal_user_assigned_departments_id_4a934b7f_fk_normal_us` FOREIGN KEY (`departments_id`) REFERENCES `normal_user_departments` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_assigneddepartments`
--

LOCK TABLES `normal_user_assigneddepartments` WRITE;
/*!40000 ALTER TABLE `normal_user_assigneddepartments` DISABLE KEYS */;
INSERT INTO `normal_user_assigneddepartments` VALUES (2,'pdf-test.pdf','/media/3/pdf-test.pdf',2);
/*!40000 ALTER TABLE `normal_user_assigneddepartments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_cities`
--

DROP TABLE IF EXISTS `normal_user_cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cities` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_cities`
--

LOCK TABLES `normal_user_cities` WRITE;
/*!40000 ALTER TABLE `normal_user_cities` DISABLE KEYS */;
INSERT INTO `normal_user_cities` VALUES (1,'gobindgarh'),(2,'Delhi');
/*!40000 ALTER TABLE `normal_user_cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_commentsmodel`
--

DROP TABLE IF EXISTS `normal_user_commentsmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_commentsmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` int(11) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `staff_user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_comments_staff_user_id_id_c17c0dcd_fk_auth_user` (`staff_user_id_id`),
  CONSTRAINT `normal_user_comments_staff_user_id_id_c17c0dcd_fk_auth_user` FOREIGN KEY (`staff_user_id_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_commentsmodel`
--

LOCK TABLES `normal_user_commentsmodel` WRITE;
/*!40000 ALTER TABLE `normal_user_commentsmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `normal_user_commentsmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_departments`
--

DROP TABLE IF EXISTS `normal_user_departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_departments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `departments` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_departments`
--

LOCK TABLES `normal_user_departments` WRITE;
/*!40000 ALTER TABLE `normal_user_departments` DISABLE KEYS */;
INSERT INTO `normal_user_departments` VALUES (1,'dept_1'),(2,'dept_2'),(3,'dept_3'),(4,'esfera'),(5,'esasda'),(6,'new_dept1'),(7,'new_dept2');
/*!40000 ALTER TABLE `normal_user_departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_emailmodel`
--

DROP TABLE IF EXISTS `normal_user_emailmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_emailmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` int(11) DEFAULT NULL,
  `subject` varchar(250) DEFAULT NULL,
  `descrtiption` varchar(250) DEFAULT NULL,
  `to_email` varchar(250) DEFAULT NULL,
  `from_email` varchar(250) DEFAULT NULL,
  `staff_user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_emailmodel_staff_user_id_id_a577ac9f_fk_auth_user_id` (`staff_user_id_id`),
  CONSTRAINT `normal_user_emailmodel_staff_user_id_id_a577ac9f_fk_auth_user_id` FOREIGN KEY (`staff_user_id_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_emailmodel`
--

LOCK TABLES `normal_user_emailmodel` WRITE;
/*!40000 ALTER TABLE `normal_user_emailmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `normal_user_emailmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_invalidattempts`
--

DROP TABLE IF EXISTS `normal_user_invalidattempts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_invalidattempts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attempts` int(11) DEFAULT NULL,
  `blocked` tinyint(1) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_invalidattempts_user_id_64cab301_fk_auth_user_id` (`user_id`),
  CONSTRAINT `normal_user_invalidattempts_user_id_64cab301_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_invalidattempts`
--

LOCK TABLES `normal_user_invalidattempts` WRITE;
/*!40000 ALTER TABLE `normal_user_invalidattempts` DISABLE KEYS */;
INSERT INTO `normal_user_invalidattempts` VALUES (1,0,0,NULL,3),(2,0,0,NULL,2),(3,0,0,NULL,1),(5,0,0,NULL,5),(6,0,0,NULL,10),(7,0,0,NULL,11),(9,0,0,NULL,13),(10,0,0,NULL,14),(14,0,0,NULL,18),(15,0,0,NULL,19),(16,0,0,NULL,20),(17,0,0,NULL,21);
/*!40000 ALTER TABLE `normal_user_invalidattempts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_managerdetails`
--

DROP TABLE IF EXISTS `normal_user_managerdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_managerdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `function` varchar(100) NOT NULL,
  `department_id` int(11) NOT NULL,
  `manaager_id` int(11) NOT NULL,
  `phone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_managerd_department_id_8927dbdf_fk_normal_us` (`department_id`),
  KEY `normal_user_managerdetails_manaager_id_d18016b9_fk_auth_user_id` (`manaager_id`),
  CONSTRAINT `normal_user_managerd_department_id_8927dbdf_fk_normal_us` FOREIGN KEY (`department_id`) REFERENCES `normal_user_departments` (`id`),
  CONSTRAINT `normal_user_managerdetails_manaager_id_d18016b9_fk_auth_user_id` FOREIGN KEY (`manaager_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_managerdetails`
--

LOCK TABLES `normal_user_managerdetails` WRITE;
/*!40000 ALTER TABLE `normal_user_managerdetails` DISABLE KEYS */;
INSERT INTO `normal_user_managerdetails` VALUES (1,'1',1,10,'5896589658'),(3,'1',1,13,'12365478987');
/*!40000 ALTER TABLE `normal_user_managerdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_managertimezones`
--

DROP TABLE IF EXISTS `normal_user_managertimezones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_managertimezones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` int(11) DEFAULT NULL,
  `timezone1` varchar(100) NOT NULL,
  `timezone2` varchar(100) NOT NULL,
  `timezone3` varchar(100) NOT NULL,
  `timezone4` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_managertimezones`
--

LOCK TABLES `normal_user_managertimezones` WRITE;
/*!40000 ALTER TABLE `normal_user_managertimezones` DISABLE KEYS */;
INSERT INTO `normal_user_managertimezones` VALUES (1,3,'Africa/Bangui','Africa/Abidjan','Africa/Djibouti','Asia/Aden'),(2,10,'Africa/Abidjan','Africa/Abidjan','Africa/Conakry','Africa/Abidjan'),(3,12,'Africa/Abidjan','Africa/Abidjan','Africa/Abidjan','Africa/Abidjan'),(4,13,'Africa/Abidjan','Africa/Abidjan','Africa/Abidjan','Africa/Abidjan');
/*!40000 ALTER TABLE `normal_user_managertimezones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_saveddocumentmodel`
--

DROP TABLE IF EXISTS `normal_user_saveddocumentmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_saveddocumentmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `path` longtext,
  `extension` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `created` datetime(6) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `csv` tinyint(1) NOT NULL,
  `doc` tinyint(1) NOT NULL,
  `docx` tinyint(1) NOT NULL,
  `jpeg` tinyint(1) NOT NULL,
  `pdf` tinyint(1) NOT NULL,
  `ppt` tinyint(1) NOT NULL,
  `xls` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_saveddocumentmodel_user_id_b23a500d_fk_auth_user_id` (`user_id`),
  CONSTRAINT `normal_user_saveddocumentmodel_user_id_b23a500d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_saveddocumentmodel`
--

LOCK TABLES `normal_user_saveddocumentmodel` WRITE;
/*!40000 ALTER TABLE `normal_user_saveddocumentmodel` DISABLE KEYS */;
INSERT INTO `normal_user_saveddocumentmodel` VALUES (5,'/media/3/sample.ppt','ppt','sample.ppt','2020-05-28 09:09:29.076356',3,0,0,0,0,0,0,0),(6,'/media/3/pdf-test.pdf','pdf','pdf-test.pdf','2020-05-28 11:57:31.064533',3,0,0,0,0,1,0,0),(8,'/media/13/TestWordDoc.doc','doc','TestWordDoc.doc','2020-05-29 05:02:09.851437',13,0,1,0,0,0,0,0);
/*!40000 ALTER TABLE `normal_user_saveddocumentmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_staffstatusmodel`
--

DROP TABLE IF EXISTS `normal_user_staffstatusmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_staffstatusmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` int(11) DEFAULT NULL,
  `status` longtext,
  `created` datetime(6) DEFAULT NULL,
  `staff_user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_staffsta_staff_user_id_id_c0c44854_fk_auth_user` (`staff_user_id_id`),
  CONSTRAINT `normal_user_staffsta_staff_user_id_id_c0c44854_fk_auth_user` FOREIGN KEY (`staff_user_id_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_staffstatusmodel`
--

LOCK TABLES `normal_user_staffstatusmodel` WRITE;
/*!40000 ALTER TABLE `normal_user_staffstatusmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `normal_user_staffstatusmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_taskmodel`
--

DROP TABLE IF EXISTS `normal_user_taskmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_taskmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` int(11) DEFAULT NULL,
  `task` longtext,
  `staff_user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_taskmodel_staff_user_id_id_eeaa92e6_fk_auth_user_id` (`staff_user_id_id`),
  CONSTRAINT `normal_user_taskmodel_staff_user_id_id_eeaa92e6_fk_auth_user_id` FOREIGN KEY (`staff_user_id_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_taskmodel`
--

LOCK TABLES `normal_user_taskmodel` WRITE;
/*!40000 ALTER TABLE `normal_user_taskmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `normal_user_taskmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_userdetails`
--

DROP TABLE IF EXISTS `normal_user_userdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_userdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` int(11) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `email2` varchar(100) NOT NULL,
  `phone_no_1` varchar(100) NOT NULL,
  `phone_no_2` varchar(100) NOT NULL,
  `timezone` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `count_timer` varchar(100) NOT NULL,
  `it_equipment_specification` varchar(100) NOT NULL,
  `comment` varchar(100) NOT NULL,
  `function` varchar(100) NOT NULL,
  `add_schedule_date_time` varchar(100) NOT NULL,
  `department_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_userdeta_department_id_e96468db_fk_normal_us` (`department_id`),
  KEY `normal_user_userdetails_user_id_cf082128_fk_auth_user_id` (`user_id`),
  CONSTRAINT `normal_user_userdeta_department_id_e96468db_fk_normal_us` FOREIGN KEY (`department_id`) REFERENCES `normal_user_departments` (`id`),
  CONSTRAINT `normal_user_userdetails_user_id_cf082128_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_userdetails`
--

LOCK TABLES `normal_user_userdetails` WRITE;
/*!40000 ALTER TABLE `normal_user_userdetails` DISABLE KEYS */;
INSERT INTO `normal_user_userdetails` VALUES (1,3,'test','abs@gmail.com','12536974858','5645613618','','esfafas','HSP','','','','','',1,2),(2,3,'','test2@asds.com','95689568956895','9568956895','Africa/Abidjan','3','3','1','25359 hjiujh nghj','tesr','3','',1,5),(3,3,'','testemp2@gmail.com','1596842371','1596842371','Africa/Abidjan','1','1','1','159862473','1596842371','1','',4,11),(8,13,'mnnji','ac@zz.zz','15963247865','689568956895','Africa/Abidjan','','1','1','','','1','',1,18),(9,3,'sfcdfv','sam2@gmail.com','8894303836','8894303838','Africa/Casablanca','','gobindgarh','3','dcdvfv','fcdvv','3','',3,19),(10,3,'sff','sam1@gmail.com','8894303836','8894303834','Africa/Addis_Ababa','','Delhi','3','dgfhb','fgfh','3','',3,20),(11,3,'sdfd','sam@gmail.com','8894303836','8894303830','Africa/Ceuta','','gobindgarh','4','fgfgn','fgbfvb','5','',6,21);
/*!40000 ALTER TABLE `normal_user_userdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user_usertype`
--

DROP TABLE IF EXISTS `normal_user_usertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normal_user_usertype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager` tinyint(1) NOT NULL,
  `normal_user` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `normal_user_usertype_user_id_f1fd27db_fk_auth_user_id` (`user_id`),
  CONSTRAINT `normal_user_usertype_user_id_f1fd27db_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user_usertype`
--

LOCK TABLES `normal_user_usertype` WRITE;
/*!40000 ALTER TABLE `normal_user_usertype` DISABLE KEYS */;
INSERT INTO `normal_user_usertype` VALUES (1,0,1,2),(2,1,0,3),(4,1,1,5),(5,0,1,11),(7,1,0,13),(8,0,1,14),(12,0,1,18),(13,0,1,19),(14,0,1,20),(15,0,1,21);
/*!40000 ALTER TABLE `normal_user_usertype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-01 16:13:42
