-- MySQL dump 10.13  Distrib 8.0.37, for Win64 (x86_64)
--
-- Host: localhost    Database: hustle
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add resource',8,'add_resource'),(30,'Can change resource',8,'change_resource'),(31,'Can delete resource',8,'delete_resource'),(32,'Can view resource',8,'view_resource'),(33,'Can add feedback',9,'add_feedback'),(34,'Can change feedback',9,'change_feedback'),(35,'Can delete feedback',9,'delete_feedback'),(36,'Can view feedback',9,'view_feedback'),(37,'Can add job listing',10,'add_joblisting'),(38,'Can change job listing',10,'change_joblisting'),(39,'Can delete job listing',10,'delete_joblisting'),(40,'Can view job listing',10,'view_joblisting'),(41,'Can add job application',11,'add_jobapplication'),(42,'Can change job application',11,'change_jobapplication'),(43,'Can delete job application',11,'delete_jobapplication'),(44,'Can view job application',11,'view_jobapplication'),(45,'Can add mentee activity',12,'add_menteeactivity'),(46,'Can change mentee activity',12,'change_menteeactivity'),(47,'Can delete mentee activity',12,'delete_menteeactivity'),(48,'Can view mentee activity',12,'view_menteeactivity'),(49,'Can add mentorship request',13,'add_mentorshiprequest'),(50,'Can change mentorship request',13,'change_mentorshiprequest'),(51,'Can delete mentorship request',13,'delete_mentorshiprequest'),(52,'Can view mentorship request',13,'view_mentorshiprequest'),(53,'Can add chat message',14,'add_chatmessage'),(54,'Can change chat message',14,'change_chatmessage'),(55,'Can delete chat message',14,'delete_chatmessage'),(56,'Can view chat message',14,'view_chatmessage'),(57,'Can add message',15,'add_message'),(58,'Can change message',15,'change_message'),(59,'Can delete message',15,'delete_message'),(60,'Can view message',15,'view_message'),(61,'Can add participant profile',16,'add_participantprofile'),(62,'Can change participant profile',16,'change_participantprofile'),(63,'Can delete participant profile',16,'delete_participantprofile'),(64,'Can view participant profile',16,'view_participantprofile'),(65,'Can add mentor profile',17,'add_mentorprofile'),(66,'Can change mentor profile',17,'change_mentorprofile'),(67,'Can delete mentor profile',17,'delete_mentorprofile'),(68,'Can view mentor profile',17,'view_mentorprofile'),(69,'Can add progress',18,'add_progress'),(70,'Can change progress',18,'change_progress'),(71,'Can delete progress',18,'delete_progress'),(72,'Can view progress',18,'view_progress'),(73,'Can add question',19,'add_question'),(74,'Can change question',19,'change_question'),(75,'Can delete question',19,'delete_question'),(76,'Can view question',19,'view_question'),(77,'Can add rating',20,'add_rating'),(78,'Can change rating',20,'change_rating'),(79,'Can delete rating',20,'delete_rating'),(80,'Can view rating',20,'view_rating'),(81,'Can add saved job',21,'add_savedjob'),(82,'Can change saved job',21,'change_savedjob'),(83,'Can delete saved job',21,'delete_savedjob'),(84,'Can view saved job',21,'view_savedjob'),(85,'Can add session',22,'add_session'),(86,'Can change session',22,'change_session'),(87,'Can delete session',22,'delete_session'),(88,'Can view session',22,'view_session'),(89,'Can add notification',23,'add_notification'),(90,'Can change notification',23,'change_notification'),(91,'Can delete notification',23,'delete_notification'),(92,'Can view notification',23,'view_notification'),(93,'Can add vote',24,'add_vote'),(94,'Can change vote',24,'change_vote'),(95,'Can delete vote',24,'delete_vote'),(96,'Can view vote',24,'view_vote'),(97,'Can add comment',25,'add_comment'),(98,'Can change comment',25,'change_comment'),(99,'Can delete comment',25,'delete_comment'),(100,'Can view comment',25,'view_comment'),(101,'Can add thread',26,'add_thread'),(102,'Can change thread',26,'change_thread'),(103,'Can delete thread',26,'delete_thread'),(104,'Can view thread',26,'view_thread'),(105,'Can add crontab',27,'add_crontabschedule'),(106,'Can change crontab',27,'change_crontabschedule'),(107,'Can delete crontab',27,'delete_crontabschedule'),(108,'Can view crontab',27,'view_crontabschedule'),(109,'Can add interval',28,'add_intervalschedule'),(110,'Can change interval',28,'change_intervalschedule'),(111,'Can delete interval',28,'delete_intervalschedule'),(112,'Can view interval',28,'view_intervalschedule'),(113,'Can add periodic task',29,'add_periodictask'),(114,'Can change periodic task',29,'change_periodictask'),(115,'Can delete periodic task',29,'delete_periodictask'),(116,'Can view periodic task',29,'view_periodictask'),(117,'Can add periodic task track',30,'add_periodictasks'),(118,'Can change periodic task track',30,'change_periodictasks'),(119,'Can delete periodic task track',30,'delete_periodictasks'),(120,'Can view periodic task track',30,'view_periodictasks'),(121,'Can add solar event',31,'add_solarschedule'),(122,'Can change solar event',31,'change_solarschedule'),(123,'Can delete solar event',31,'delete_solarschedule'),(124,'Can view solar event',31,'view_solarschedule'),(125,'Can add clocked',32,'add_clockedschedule'),(126,'Can change clocked',32,'change_clockedschedule'),(127,'Can delete clocked',32,'delete_clockedschedule'),(128,'Can view clocked',32,'view_clockedschedule'),(129,'Can add certificate',33,'add_certificate'),(130,'Can change certificate',33,'change_certificate'),(131,'Can delete certificate',33,'delete_certificate'),(132,'Can view certificate',33,'view_certificate');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_certificate`
--

DROP TABLE IF EXISTS `capstone_certificate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_certificate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `certificate_file` varchar(100) NOT NULL,
  `issued_at` datetime(6) NOT NULL,
  `mentor_id` bigint NOT NULL,
  `participant_id` bigint NOT NULL,
  `resource_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_certificate_mentor_id_b531739e_fk_capstone_user_id` (`mentor_id`),
  KEY `capstone_certificate_participant_id_0092fc05_fk_capstone_user_id` (`participant_id`),
  KEY `capstone_certificate_resource_id_bbfb9062_fk_capstone_` (`resource_id`),
  CONSTRAINT `capstone_certificate_mentor_id_b531739e_fk_capstone_user_id` FOREIGN KEY (`mentor_id`) REFERENCES `capstone_user` (`id`),
  CONSTRAINT `capstone_certificate_participant_id_0092fc05_fk_capstone_user_id` FOREIGN KEY (`participant_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_certificate`
--

LOCK TABLES `capstone_certificate` WRITE;
/*!40000 ALTER TABLE `capstone_certificate` DISABLE KEYS */;
INSERT INTO `capstone_certificate` VALUES (14,'certificates/certificate_Ardine Martine NUKURI_7.pdf','2025-02-12 13:53:19.697954',9,8,7);
/*!40000 ALTER TABLE `capstone_certificate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_chapter`
--

DROP TABLE IF EXISTS `capstone_chapter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_chapter` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `chapter_number` int unsigned NOT NULL,
  `is_completed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `capstone_chapter_chk_1` CHECK ((`chapter_number` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_chapter`
--

LOCK TABLES `capstone_chapter` WRITE;
/*!40000 ALTER TABLE `capstone_chapter` DISABLE KEYS */;
/*!40000 ALTER TABLE `capstone_chapter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_chatmessage`
--

DROP TABLE IF EXISTS `capstone_chatmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_chatmessage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `sender_id` bigint NOT NULL,
  `mentorship_request_id` bigint NOT NULL,
  `downvotes` int NOT NULL,
  `upvotes` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_chatmessage_sender_id_e72951af_fk_capstone_user_id` (`sender_id`),
  KEY `capstone_chatmessage_mentorship_request_i_0d8503ad_fk_capstone_` (`mentorship_request_id`),
  CONSTRAINT `capstone_chatmessage_mentorship_request_i_0d8503ad_fk_capstone_` FOREIGN KEY (`mentorship_request_id`) REFERENCES `capstone_mentorshiprequest` (`id`),
  CONSTRAINT `capstone_chatmessage_sender_id_e72951af_fk_capstone_user_id` FOREIGN KEY (`sender_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_chatmessage`
--

LOCK TABLES `capstone_chatmessage` WRITE;
/*!40000 ALTER TABLE `capstone_chatmessage` DISABLE KEYS */;
INSERT INTO `capstone_chatmessage` VALUES (1,'hello gys','2025-02-03 00:50:56.657058',9,5,0,0),(2,'hy','2025-02-03 09:28:11.008645',8,1,0,1),(3,'hy','2025-02-03 22:08:52.519061',8,1,0,0),(4,'hy, how can I help you?','2025-02-03 23:23:26.167136',9,7,0,0),(5,'hy, how are you?','2025-02-04 21:35:21.508044',9,8,0,0);
/*!40000 ALTER TABLE `capstone_chatmessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_comment`
--

DROP TABLE IF EXISTS `capstone_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `upvotes` int NOT NULL,
  `downvotes` int NOT NULL,
  `user_id` bigint NOT NULL,
  `thread_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_comment_user_id_a2192c33_fk_capstone_user_id` (`user_id`),
  KEY `capstone_comment_thread_id_d1fd5d28_fk_capstone_thread_id` (`thread_id`),
  CONSTRAINT `capstone_comment_thread_id_d1fd5d28_fk_capstone_thread_id` FOREIGN KEY (`thread_id`) REFERENCES `capstone_thread` (`id`),
  CONSTRAINT `capstone_comment_user_id_a2192c33_fk_capstone_user_id` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_comment`
--

LOCK TABLES `capstone_comment` WRITE;
/*!40000 ALTER TABLE `capstone_comment` DISABLE KEYS */;
INSERT INTO `capstone_comment` VALUES (12,'okay that\'s so nice','2025-02-04 08:57:36.233323','2025-02-05 00:01:29.922551',1,1,8,1),(17,'you\'re right\r\n','2025-02-11 21:59:57.069096','2025-02-11 21:59:57.069096',0,0,8,2);
/*!40000 ALTER TABLE `capstone_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_feedback`
--

DROP TABLE IF EXISTS `capstone_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` double NOT NULL,
  `feedback` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `mentee_id` bigint NOT NULL,
  `mentor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_feedback_mentee_id_4e3c9aa5_fk_capstone_user_id` (`mentee_id`),
  KEY `capstone_feedback_mentor_id_719e2998_fk_capstone_user_id` (`mentor_id`),
  CONSTRAINT `capstone_feedback_mentee_id_4e3c9aa5_fk_capstone_user_id` FOREIGN KEY (`mentee_id`) REFERENCES `capstone_user` (`id`),
  CONSTRAINT `capstone_feedback_mentor_id_719e2998_fk_capstone_user_id` FOREIGN KEY (`mentor_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_feedback`
--

LOCK TABLES `capstone_feedback` WRITE;
/*!40000 ALTER TABLE `capstone_feedback` DISABLE KEYS */;
INSERT INTO `capstone_feedback` VALUES (1,3,'','2025-02-06 11:27:37.410618',8,9),(2,4,'you are a such great mentor','2025-02-06 12:27:15.911605',8,9);
/*!40000 ALTER TABLE `capstone_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_jobapplication`
--

DROP TABLE IF EXISTS `capstone_jobapplication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_jobapplication` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(20) NOT NULL,
  `applied_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `job_listing_id` bigint NOT NULL,
  `cover_letter` longtext NOT NULL DEFAULT (_utf8mb3'Cover letter not provided.'),
  `resume` varchar(100) NOT NULL,
  `accepted_by_mentor_email` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_jobapplication_user_id_251de6fd_fk_capstone_user_id` (`user_id`),
  KEY `capstone_jobapplicat_job_listing_id_2c18ebca_fk_capstone_` (`job_listing_id`),
  CONSTRAINT `capstone_jobapplicat_job_listing_id_2c18ebca_fk_capstone_` FOREIGN KEY (`job_listing_id`) REFERENCES `capstone_joblisting` (`id`),
  CONSTRAINT `capstone_jobapplication_user_id_251de6fd_fk_capstone_user_id` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_jobapplication`
--

LOCK TABLES `capstone_jobapplication` WRITE;
/*!40000 ALTER TABLE `capstone_jobapplication` DISABLE KEYS */;
INSERT INTO `capstone_jobapplication` VALUES (2,'accepted','2025-02-06 14:44:04.826710',8,3,'class JobSubmitForm(forms.ModelForm):\r\n    class Meta:\r\n        model = JobApplication\r\n        fields = [\'resume\', \'cover_letter\']\r\n\r\n    resume = forms.FileField(\r\n        required=True,\r\n        widget=forms.ClearableFileInput(attrs={\'class\': \'form-control\', \'accept\': \'.pdf\'}),\r\n        label=\"Upload Resume (PDF)\"\r\n    )\r\n\r\n    cover_letter = forms.CharField(\r\n        widget=forms.Textarea(attrs={\'class\': \'form-control\', \'rows\': 4}),\r\n        required=True\r\n    )class JobSubmitForm(forms.ModelForm):\r\n    class Meta:\r\n        model = JobApplication\r\n        fields = [\'resume\', \'cover_letter\']\r\n\r\n    resume = forms.FileField(\r\n        required=True,\r\n        widget=forms.ClearableFileInput(attrs={\'class\': \'form-control\', \'accept\': \'.pdf\'}),\r\n        label=\"Upload Resume (PDF)\"\r\n    )\r\n\r\n    cover_letter = forms.CharField(\r\n        widget=forms.Textarea(attrs={\'class\': \'form-control\', \'rows\': 4}),\r\n        required=True\r\n    )','resumes/EALA-Symposium-Harelimana_RVyVHxy.pdf',NULL),(3,'rejected','2025-02-06 21:31:16.186477',11,3,'My MenteesMy MenteesMy MenteesMy MenteesMy MenteesMy MenteesMy MenteesMy Mentees','resumes/EAC_DEBATE_FORMAT_DRAFT_nUBwdYw.pdf',NULL),(4,'accepted','2025-02-06 23:21:27.592368',11,2,'@login_required\r\ndef apply_for_job(request, job_id):\r\n    job_listing = get_object_or_404(JobListing, id=job_id)\r\n    mentor = job_listing.employer  # ✅ Get the mentor (employer) who posted the job\r\n\r\n    if request.method == \'POST\':\r\n        print(\"POST request received!\")  # ✅ Debugging\r\n        print(\"POST Data:\", request.POST)  # ✅ Show POST data\r\n        print(\"FILES Data:\", request.FILES)  # ✅ Show FILES data\r\n\r\n        form = JobSubmitForm(request.POST, request.FILES)  # ✅ Include request.FILES\r\n        if form.is_valid():\r\n            print(\"Form is valid!\")  # ✅ Check if form is valid\r\n            job_application = form.save(commit=False)\r\n            job_application.user = request.user\r\n            job_application.job_listing = job_listing\r\n            job_application.save()\r\n            print(\"Job application saved!\")  # ✅ Check if application is saved\r\n\r\n            # ✅ Create a notification for the mentor\r\n            Notification.objects.create(\r\n                user=mentor,  # ✅ Corrected: Assign the actual mentor (User instance)\r\n                message=f\"{request.user.full_name} has applied for your job listing: {job_listing.title}.\"\r\n            )\r\n\r\n            return redirect(\'job_application_tracker\')  # Redirect after applying\r\n        else:\r\n            print(\"Form Errors:\", form.errors)  # ✅ Print form validation errors\r\n\r\n    else:\r\n        form = JobSubmitForm(initial={\'job_listing\': job_listing})\r\n\r\n    return render(request, \'capstone/apply_for_job.html\', {\r\n        \'form\': form,\r\n        \'job_listing\': job_listing,\r\n    })','resumes/2013_EAC_youth_policy_tX64m4L.pdf','nukuriardinemartine@gmail.com'),(5,'rejected','2025-02-07 00:00:18.268704',11,3,'hello hello hello hello hello hello','resumes/Progress_towards_EAC_Political_Integration_1999-2018.pdf',NULL),(7,'accepted','2025-02-07 17:42:39.377800',8,3,'I really need this job','resumes/A.M.N_-_CV.pdf',NULL),(8,'submitted','2025-02-11 11:16:54.954258',8,3,'okay okay okay okay okay okay okay okay okay okay','resumes/certificate_Ardine_Martine_NUKURI_2.pdf',NULL),(9,'submitted','2025-02-12 14:09:08.086756',8,3,'olololololoo','resumes/NukuriMartineArdineAPPLICATIONFOREQUATINGFOREIGNQUALIFICATIONS-GENERALEDUCATION-_PnTtHOS.pdf',NULL);
/*!40000 ALTER TABLE `capstone_jobapplication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_joblisting`
--

DROP TABLE IF EXISTS `capstone_joblisting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_joblisting` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `location` varchar(100) NOT NULL,
  `industry` varchar(100) NOT NULL,
  `job_type` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `employer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_joblisting_employer_id_c3cb59be_fk_capstone_user_id` (`employer_id`),
  CONSTRAINT `capstone_joblisting_employer_id_c3cb59be_fk_capstone_user_id` FOREIGN KEY (`employer_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_joblisting`
--

LOCK TABLES `capstone_joblisting` WRITE;
/*!40000 ALTER TABLE `capstone_joblisting` DISABLE KEYS */;
INSERT INTO `capstone_joblisting` VALUES (2,'Photographer','We need a special photographer','Bujumbura','Now Studio','part_time','2025-02-06 00:30:58.273576',10),(3,'Receptionist','Receptionist','Gitega','Green Park Resort','full_time','2025-02-06 10:18:00.359236',9);
/*!40000 ALTER TABLE `capstone_joblisting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_menteeactivity`
--

DROP TABLE IF EXISTS `capstone_menteeactivity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_menteeactivity` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `activity` varchar(255) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `mentor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_menteeactivity_mentor_id_6fef2984_fk_capstone_user_id` (`mentor_id`),
  CONSTRAINT `capstone_menteeactivity_mentor_id_6fef2984_fk_capstone_user_id` FOREIGN KEY (`mentor_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_menteeactivity`
--

LOCK TABLES `capstone_menteeactivity` WRITE;
/*!40000 ALTER TABLE `capstone_menteeactivity` DISABLE KEYS */;
/*!40000 ALTER TABLE `capstone_menteeactivity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_mentorprofile`
--

DROP TABLE IF EXISTS `capstone_mentorprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_mentorprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bio` longtext,
  `expertise_areas` longtext,
  `feedback` longtext,
  `rating` double NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `capstone_mentorprofile_user_id_fea8af13_fk_capstone_user_id` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_mentorprofile`
--

LOCK TABLES `capstone_mentorprofile` WRITE;
/*!40000 ALTER TABLE `capstone_mentorprofile` DISABLE KEYS */;
INSERT INTO `capstone_mentorprofile` VALUES (1,'Specialized in Pschlogy','',NULL,0,9),(2,NULL,NULL,NULL,0,8),(3,NULL,NULL,NULL,0,10),(4,NULL,NULL,NULL,0,11);
/*!40000 ALTER TABLE `capstone_mentorprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_mentorprofile_mentees`
--

DROP TABLE IF EXISTS `capstone_mentorprofile_mentees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_mentorprofile_mentees` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mentorprofile_id` bigint NOT NULL,
  `participantprofile_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `capstone_mentorprofile_m_mentorprofile_id_partici_9c5be8d4_uniq` (`mentorprofile_id`,`participantprofile_id`),
  KEY `capstone_mentorprofi_participantprofile_i_89203ad4_fk_capstone_` (`participantprofile_id`),
  CONSTRAINT `capstone_mentorprofi_mentorprofile_id_c6768c30_fk_capstone_` FOREIGN KEY (`mentorprofile_id`) REFERENCES `capstone_mentorprofile` (`id`),
  CONSTRAINT `capstone_mentorprofi_participantprofile_i_89203ad4_fk_capstone_` FOREIGN KEY (`participantprofile_id`) REFERENCES `capstone_participantprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_mentorprofile_mentees`
--

LOCK TABLES `capstone_mentorprofile_mentees` WRITE;
/*!40000 ALTER TABLE `capstone_mentorprofile_mentees` DISABLE KEYS */;
/*!40000 ALTER TABLE `capstone_mentorprofile_mentees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_mentorshiprequest`
--

DROP TABLE IF EXISTS `capstone_mentorshiprequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_mentorshiprequest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `mentee_id` bigint NOT NULL,
  `mentor_id` bigint NOT NULL,
  `mentor_response` longtext,
  PRIMARY KEY (`id`),
  KEY `capstone_mentorshipr_mentee_id_a9de5569_fk_capstone_` (`mentee_id`),
  KEY `capstone_mentorshipr_mentor_id_b061c0d3_fk_capstone_` (`mentor_id`),
  CONSTRAINT `capstone_mentorshipr_mentee_id_a9de5569_fk_capstone_` FOREIGN KEY (`mentee_id`) REFERENCES `capstone_user` (`id`),
  CONSTRAINT `capstone_mentorshipr_mentor_id_b061c0d3_fk_capstone_` FOREIGN KEY (`mentor_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_mentorshiprequest`
--

LOCK TABLES `capstone_mentorshiprequest` WRITE;
/*!40000 ALTER TABLE `capstone_mentorshiprequest` DISABLE KEYS */;
INSERT INTO `capstone_mentorshiprequest` VALUES (1,'I really need your help','approved','2025-02-03 00:06:15.048801',8,9,NULL),(2,'I really need your help','approved','2025-02-03 00:07:10.077433',8,9,NULL),(3,'I really need your help, is there any way. we can discuss','approved','2025-02-03 00:07:44.607909',8,9,NULL),(4,'How can we meet?','declined','2025-02-03 00:13:37.807024',8,9,NULL),(5,'I really need your help','approved','2025-02-03 00:50:17.730110',8,9,'Yes Ardine, I\'m here to help you Can schedule a meeting Or DM me on my email'),(6,'i want your help','approved','2025-02-03 10:06:25.566100',8,9,'okay, you can schedule a session with me'),(7,'Hy, can we meet?','approved','2025-02-03 23:22:49.131470',8,9,'it\'s okay you can schedule a meeting on google calendar you already have my email'),(8,'hy','declined','2025-02-04 21:34:14.287630',8,9,'I\'m sorry, I\'m not available Ardine. But if you don\'t mid you can schedule a meeting by friday on google meet. I will be available from 8 to 11 am'),(9,'okay','approved','2025-02-05 20:49:00.733220',8,9,''),(10,'Hy, I want to schedule a meeting with you','declined','2025-02-05 20:58:43.704651',8,9,''),(11,'Hy can you be my mentor??','approved','2025-02-05 23:50:13.373768',8,10,'It\'s Okay Ardine , I can mentor you'),(12,'hy','approved','2025-02-06 00:27:32.634659',8,10,'okay'),(13,'Hy, can you bee my supervisor?','approved','2025-02-06 10:46:18.588518',8,9,'of cource Ardine, I would like too!'),(14,'Hy, I really in need of mentorship. Can you bee my supervisor?','approved','2025-02-06 13:07:39.764975',11,9,'It\'s okay Erica. I can mentor you. You can dm me in google chat'),(15,'Hello, I reaaly need help, can you my mentor?','declined','2025-02-11 11:13:59.677429',8,9,'I\'m not available, sorry'),(16,'hy','pending','2025-02-12 14:08:22.932905',8,9,NULL);
/*!40000 ALTER TABLE `capstone_mentorshiprequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_message`
--

DROP TABLE IF EXISTS `capstone_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `mentor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_message_mentor_id_e84c39f6_fk_capstone_user_id` (`mentor_id`),
  CONSTRAINT `capstone_message_mentor_id_e84c39f6_fk_capstone_user_id` FOREIGN KEY (`mentor_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_message`
--

LOCK TABLES `capstone_message` WRITE;
/*!40000 ALTER TABLE `capstone_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `capstone_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_notification`
--

DROP TABLE IF EXISTS `capstone_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `is_seen` tinyint(1) NOT NULL,
  `job_application_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_notification_user_id_9b71723e_fk_capstone_user_id` (`user_id`),
  KEY `capstone_notificatio_job_application_id_c292715d_fk_capstone_` (`job_application_id`),
  CONSTRAINT `capstone_notificatio_job_application_id_c292715d_fk_capstone_` FOREIGN KEY (`job_application_id`) REFERENCES `capstone_jobapplication` (`id`),
  CONSTRAINT `capstone_notification_user_id_9b71723e_fk_capstone_user_id` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_notification`
--

LOCK TABLES `capstone_notification` WRITE;
/*!40000 ALTER TABLE `capstone_notification` DISABLE KEYS */;
INSERT INTO `capstone_notification` VALUES (1,'A session has been scheduled with Ardine Martine NUKURI on 2025-01-03 00:00:00+00:00.',0,'2025-02-03 10:01:57.070277',9,0,NULL),(2,'A new resource has been uploaded: <django.db.models.query_utils.DeferredAttribute object at 0x000001F53ACA9850>',0,'2025-02-03 10:04:04.581845',8,1,NULL),(3,'Your mentorship request has been approved by edith Uwase. Response: okay, you can schedule a session with me',0,'2025-02-03 10:07:26.030413',8,1,NULL),(4,'Your mentorship request has been approved by edith Uwase. Response: it\'s okay you can schedule a meeting on google calendar you already have my email',0,'2025-02-03 23:36:49.434948',8,1,NULL),(5,'A new resource has been uploaded: <django.db.models.query_utils.DeferredAttribute object at 0x0000022B5CA76180>',0,'2025-02-04 23:20:25.711582',8,1,NULL),(6,'Your mentorship request has been declined by edith Uwase. Response: I\'m sorry, I\'m not available Ardine. But if you don\'t mid you can schedule a meeting by friday on google meet. I will be available from 8 to 11 am',0,'2025-02-05 21:01:38.565186',8,1,NULL),(7,'Your mentorship request has been approved by edith Uwase. Response: ',0,'2025-02-05 21:05:57.441848',8,1,NULL),(8,'Your mentorship request has been declined by edith Uwase. Response: ',0,'2025-02-05 21:06:01.132330',8,1,NULL),(9,'Your mentorship request has been approved by Doune Manirakiza!',0,'2025-02-05 23:51:45.616214',8,1,NULL),(10,'Your mentorship request has been approved by Doune Manirakiza. Response: okay',0,'2025-02-06 00:28:10.468306',8,1,NULL),(11,'A new resource has been uploaded: <django.db.models.query_utils.DeferredAttribute object at 0x0000023E0D31AD80>',0,'2025-02-06 10:14:09.838453',8,1,NULL),(12,'A new job has been posted: Receptionist.',0,'2025-02-06 10:18:00.377865',8,1,NULL),(13,'Your mentorship request has been approved by edith Uwase. Response: of cource Ardine, I would like too!',0,'2025-02-06 10:46:54.077570',8,0,NULL),(14,'A new resource has been uploaded',0,'2025-02-06 11:16:10.506009',8,0,NULL),(15,'Your mentorship request has been approved by edith Uwase. Response: It\'s okay Erica. I can mentor you. You can dm me in google chat',0,'2025-02-06 13:08:29.991152',11,1,NULL),(16,'Erica-Livia Ingabire has applied for your job listing: Photographer.',0,'2025-02-06 23:21:27.660052',10,1,NULL),(17,'Erica-Livia Ingabire has applied for your job listing: Receptionist.',0,'2025-02-07 00:00:18.356001',9,1,5),(19,'Your application for \'Makeup Artist\' has been accepted.',0,'2025-02-07 11:06:10.527058',8,0,NULL),(20,'Your application for \'Receptionist\' has been rejected.',0,'2025-02-07 11:09:56.072127',11,0,NULL),(21,'Your application for \'Receptionist\' has been rejected.',0,'2025-02-07 11:10:38.237499',11,1,NULL),(22,'Your application for \'Receptionist\' has been accepted.',0,'2025-02-07 11:10:50.998168',8,0,NULL),(23,'Ardine Martine NUKURI has applied for your job listing: Receptionist.',0,'2025-02-07 17:42:39.405095',9,1,7),(24,'Your application for \'Receptionist\' has been accepted.',0,'2025-02-07 18:55:16.257552',8,0,NULL),(25,'Your application for \'Photographer\' has been accepted.',0,'2025-02-07 19:03:59.849552',11,0,NULL),(26,'A new resource has been uploaded',0,'2025-02-10 15:14:58.995315',8,1,NULL),(27,'A new resource has been uploaded',0,'2025-02-10 15:14:59.003323',11,0,NULL),(28,'Ardine Martine NUKURI has applied for your job listing: Receptionist.',0,'2025-02-11 11:16:55.008324',9,1,8),(29,'Your mentorship request has been declined by edith Uwase. Response: I\'m not available, sorry',0,'2025-02-11 11:19:46.128254',8,0,NULL),(30,'A new resource has been uploaded',0,'2025-02-11 11:57:49.770130',8,0,NULL),(31,'A new resource has been uploaded',0,'2025-02-11 11:57:49.779726',11,0,NULL),(32,'Ardine Martine NUKURI has applied for your job listing: Receptionist.',0,'2025-02-12 14:09:08.152061',9,0,9);
/*!40000 ALTER TABLE `capstone_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_participantprofile`
--

DROP TABLE IF EXISTS `capstone_participantprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_participantprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bio` longtext,
  `skills` longtext,
  `interests` longtext,
  `certifications` varchar(100) DEFAULT NULL,
  `mentor_id` bigint DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `capstone_participant_mentor_id_02a1d092_fk_capstone_` (`mentor_id`),
  CONSTRAINT `capstone_participant_mentor_id_02a1d092_fk_capstone_` FOREIGN KEY (`mentor_id`) REFERENCES `capstone_user` (`id`),
  CONSTRAINT `capstone_participantprofile_user_id_1227569a_fk_capstone_user_id` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_participantprofile`
--

LOCK TABLES `capstone_participantprofile` WRITE;
/*!40000 ALTER TABLE `capstone_participantprofile` DISABLE KEYS */;
INSERT INTO `capstone_participantprofile` VALUES (1,'I\'m burundian','html','Mentorship','certifications/wcms_732716.pdf',9,8),(2,NULL,NULL,NULL,'',NULL,9),(3,NULL,NULL,NULL,'',NULL,10),(4,NULL,NULL,NULL,'',9,11);
/*!40000 ALTER TABLE `capstone_participantprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_progress`
--

DROP TABLE IF EXISTS `capstone_progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_progress` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `task` varchar(255) NOT NULL,
  `completed` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `participant_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_progress_participant_id_dc4f9466_fk_capstone_user_id` (`participant_id`),
  CONSTRAINT `capstone_progress_participant_id_dc4f9466_fk_capstone_user_id` FOREIGN KEY (`participant_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_progress`
--

LOCK TABLES `capstone_progress` WRITE;
/*!40000 ALTER TABLE `capstone_progress` DISABLE KEYS */;
/*!40000 ALTER TABLE `capstone_progress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_question`
--

DROP TABLE IF EXISTS `capstone_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_question` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `mentor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_question_mentor_id_628206ae_fk_capstone_user_id` (`mentor_id`),
  CONSTRAINT `capstone_question_mentor_id_628206ae_fk_capstone_user_id` FOREIGN KEY (`mentor_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_question`
--

LOCK TABLES `capstone_question` WRITE;
/*!40000 ALTER TABLE `capstone_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `capstone_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_rating`
--

DROP TABLE IF EXISTS `capstone_rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_rating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` double NOT NULL,
  `review` longtext,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `resource_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_rating_user_id_9c42136d_fk_capstone_user_id` (`user_id`),
  KEY `capstone_rating_resource_id_8e1bf894_fk_capstone_resource_id` (`resource_id`),
  CONSTRAINT `capstone_rating_user_id_9c42136d_fk_capstone_user_id` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_rating`
--

LOCK TABLES `capstone_rating` WRITE;
/*!40000 ALTER TABLE `capstone_rating` DISABLE KEYS */;
INSERT INTO `capstone_rating` VALUES (4,3,'it\'s  a good resource','2025-02-10 15:23:19.575576',8,2),(5,5,'it\'s a good resource','2025-02-10 18:16:54.570540',8,2),(6,3,'okay','2025-02-10 18:29:33.377499',8,2),(7,8,'','2025-02-10 18:35:09.268281',11,2),(8,5,'this is a good resource','2025-02-11 11:15:51.424264',8,2);
/*!40000 ALTER TABLE `capstone_rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_savedjob`
--

DROP TABLE IF EXISTS `capstone_savedjob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_savedjob` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `saved_at` datetime(6) NOT NULL,
  `job_listing_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_savedjob_job_listing_id_c8e3db3f_fk_capstone_` (`job_listing_id`),
  KEY `capstone_savedjob_user_id_8d43cf01_fk_capstone_user_id` (`user_id`),
  CONSTRAINT `capstone_savedjob_job_listing_id_c8e3db3f_fk_capstone_` FOREIGN KEY (`job_listing_id`) REFERENCES `capstone_joblisting` (`id`),
  CONSTRAINT `capstone_savedjob_user_id_8d43cf01_fk_capstone_user_id` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_savedjob`
--

LOCK TABLES `capstone_savedjob` WRITE;
/*!40000 ALTER TABLE `capstone_savedjob` DISABLE KEYS */;
/*!40000 ALTER TABLE `capstone_savedjob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_session`
--

DROP TABLE IF EXISTS `capstone_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `scheduled_time` datetime(6) NOT NULL,
  `notes` longtext,
  `created_at` datetime(6) NOT NULL,
  `mentorship_request_id` bigint NOT NULL,
  `mentor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_session_mentorship_request_i_e557cb8e_fk_capstone_` (`mentorship_request_id`),
  KEY `capstone_session_mentor_id_3cd34f47_fk_capstone_user_id` (`mentor_id`),
  CONSTRAINT `capstone_session_mentor_id_3cd34f47_fk_capstone_user_id` FOREIGN KEY (`mentor_id`) REFERENCES `capstone_user` (`id`),
  CONSTRAINT `capstone_session_mentorship_request_i_e557cb8e_fk_capstone_` FOREIGN KEY (`mentorship_request_id`) REFERENCES `capstone_mentorshiprequest` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_session`
--

LOCK TABLES `capstone_session` WRITE;
/*!40000 ALTER TABLE `capstone_session` DISABLE KEYS */;
INSERT INTO `capstone_session` VALUES (1,'2025-01-03 00:00:00.000000','','2025-02-03 10:01:57.059761',1,9),(2,'2025-02-03 12:00:00.000000','fdhis','2025-02-03 20:55:05.258074',1,9),(3,'2025-02-14 16:00:00.000000','this time would favorite me','2025-02-03 22:10:09.579386',2,9),(4,'2025-02-05 09:00:00.000000','','2025-02-03 22:52:05.601742',2,8),(5,'2025-02-05 09:00:00.000000','','2025-02-03 22:54:02.644543',2,8),(6,'2025-02-12 12:00:00.000000','','2025-02-03 22:58:46.208953',2,9),(7,'2025-02-07 12:00:00.000000','','2025-02-03 23:12:41.742999',1,9),(8,'2025-02-05 12:00:00.000000','Is this day okay with you','2025-02-05 13:19:35.105377',1,9),(9,'2025-02-05 12:00:00.000000','okay','2025-02-05 14:35:54.567155',1,9),(10,'2025-02-05 12:00:00.000000','okay','2025-02-05 14:42:52.848560',1,9),(11,'2025-02-11 12:00:00.000000','okay','2025-02-05 15:32:23.219901',1,9),(12,'2025-02-11 12:00:00.000000','okay','2025-02-05 15:39:09.007810',1,9),(13,'2025-02-18 12:00:00.000000','okay','2025-02-05 15:43:59.765248',1,9),(14,'2025-02-11 12:00:00.000000','okay','2025-02-05 20:42:35.141450',1,10);
/*!40000 ALTER TABLE `capstone_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_thread`
--

DROP TABLE IF EXISTS `capstone_thread`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_thread` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `tags` varchar(100) NOT NULL,
  `created_by_id` bigint NOT NULL,
  `downvotes` int NOT NULL,
  `upvotes` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `capstone_thread_created_by_id_3819a897_fk_capstone_user_id` (`created_by_id`),
  CONSTRAINT `capstone_thread_created_by_id_3819a897_fk_capstone_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_thread`
--

LOCK TABLES `capstone_thread` WRITE;
/*!40000 ALTER TABLE `capstone_thread` DISABLE KEYS */;
INSERT INTO `capstone_thread` VALUES (1,'Empowering Women Through Education: A Catalyst for Change','Most of the times we think that empowering women is just giving them the jobs. But it\'s better to teach you how to get money more than giving you money','2025-02-04 00:26:14.959748','2025-02-04 00:26:14.959748','',8,0,0),(2,'L\'union fait la force','L\'union fait la force','2025-02-04 00:39:45.643841','2025-02-11 10:55:57.374862','',9,5,4);
/*!40000 ALTER TABLE `capstone_thread` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_user`
--

DROP TABLE IF EXISTS `capstone_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `terms_accepted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_user`
--

LOCK TABLES `capstone_user` WRITE;
/*!40000 ALTER TABLE `capstone_user` DISABLE KEYS */;
INSERT INTO `capstone_user` VALUES (8,'pbkdf2_sha256$870000$HvoY5lgFe5yRxMBP6y8FqR$SgwYbaB3WuuxTZ6zgbodL4pNujjQD3rKmMRuoX8KCmM=','2025-02-12 14:08:48.422266',0,'Ardy','','',0,1,'2025-02-01 14:30:18.979371','Ardine Martine NUKURI','ardinemartinenukuri@gmail.com','71020942','participant',0),(9,'pbkdf2_sha256$870000$obRnI3YEFDYbSCRRCNGvyI$f97JAQqHGSmDPPgJ+a2Ovffn3FOIhUu68eZFyOvQNIM=','2025-02-12 23:40:09.369614',0,'Edith','','',0,1,'2025-02-01 15:00:03.123837','edith Uwase','e.uwase@alustudent.com','71020942','mentor',0),(10,'pbkdf2_sha256$870000$P5ckh1KfxgP9FnGn6hn7XT$XuvQi7ftgrC0MWz14WeabxqpLjm0HTdhK5FKG/V80Kg=','2025-02-07 19:03:36.248996',0,'Doune','','',0,1,'2025-02-05 16:10:48.619222','Doune Manirakiza','nukuriardinemartine@gmail.com','71020942','mentor',0),(11,'pbkdf2_sha256$870000$7LDM7GfEmrj3nigLDLeyQn$wltH807E1eLiqwmv7Vl7OS1UxuZoDmTmLgG2mpIfqEA=','2025-02-10 18:34:56.091573',0,'Erica-Livia','','',0,1,'2025-02-06 13:05:50.729964','Erica-Livia Ingabire','ericaliviaingabire@gmail.com','0790135713','participant',0);
/*!40000 ALTER TABLE `capstone_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_user_groups`
--

DROP TABLE IF EXISTS `capstone_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `capstone_user_groups_user_id_group_id_7eec89da_uniq` (`user_id`,`group_id`),
  KEY `capstone_user_groups_group_id_465aef3b_fk_auth_group_id` (`group_id`),
  CONSTRAINT `capstone_user_groups_group_id_465aef3b_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `capstone_user_groups_user_id_a107f5b7_fk_capstone_user_id` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_user_groups`
--

LOCK TABLES `capstone_user_groups` WRITE;
/*!40000 ALTER TABLE `capstone_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `capstone_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_user_user_permissions`
--

DROP TABLE IF EXISTS `capstone_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `capstone_user_user_permi_user_id_permission_id_722ad3d8_uniq` (`user_id`,`permission_id`),
  KEY `capstone_user_user_p_permission_id_13194176_fk_auth_perm` (`permission_id`),
  CONSTRAINT `capstone_user_user_p_permission_id_13194176_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `capstone_user_user_p_user_id_55331e4e_fk_capstone_` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_user_user_permissions`
--

LOCK TABLES `capstone_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `capstone_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `capstone_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capstone_vote`
--

DROP TABLE IF EXISTS `capstone_vote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capstone_vote` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `vote_type` varchar(10) NOT NULL,
  `comment_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `capstone_vote_user_id_comment_id_eb3ea4ca_uniq` (`user_id`,`comment_id`),
  KEY `capstone_vote_comment_id_013872a0_fk_capstone_comment_id` (`comment_id`),
  CONSTRAINT `capstone_vote_comment_id_013872a0_fk_capstone_comment_id` FOREIGN KEY (`comment_id`) REFERENCES `capstone_comment` (`id`),
  CONSTRAINT `capstone_vote_user_id_10e090c0_fk_capstone_user_id` FOREIGN KEY (`user_id`) REFERENCES `capstone_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capstone_vote`
--

LOCK TABLES `capstone_vote` WRITE;
/*!40000 ALTER TABLE `capstone_vote` DISABLE KEYS */;
INSERT INTO `capstone_vote` VALUES (12,'downvote',12,8),(13,'upvote',12,9);
/*!40000 ALTER TABLE `capstone_vote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_clockedschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_clockedschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_clockedschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `clocked_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_clockedschedule`
--

LOCK TABLES `django_celery_beat_clockedschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_clockedschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_clockedschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_crontabschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_crontabschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_crontabschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `minute` varchar(240) NOT NULL,
  `hour` varchar(96) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(124) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  `timezone` varchar(63) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_crontabschedule`
--

LOCK TABLES `django_celery_beat_crontabschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_intervalschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_intervalschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_intervalschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `every` int NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_intervalschedule`
--

LOCK TABLES `django_celery_beat_intervalschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictask`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_periodictask` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int unsigned NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int DEFAULT NULL,
  `interval_id` int DEFAULT NULL,
  `solar_id` int DEFAULT NULL,
  `one_off` tinyint(1) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `priority` int unsigned DEFAULT NULL,
  `headers` longtext NOT NULL DEFAULT (_utf8mb3'{}'),
  `clocked_id` int DEFAULT NULL,
  `expire_seconds` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` (`crontab_id`),
  KEY `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` (`interval_id`),
  KEY `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` (`solar_id`),
  KEY `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` (`clocked_id`),
  CONSTRAINT `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` FOREIGN KEY (`clocked_id`) REFERENCES `django_celery_beat_clockedschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` FOREIGN KEY (`crontab_id`) REFERENCES `django_celery_beat_crontabschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` FOREIGN KEY (`interval_id`) REFERENCES `django_celery_beat_intervalschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` FOREIGN KEY (`solar_id`) REFERENCES `django_celery_beat_solarschedule` (`id`),
  CONSTRAINT `django_celery_beat_periodictask_chk_1` CHECK ((`total_run_count` >= 0)),
  CONSTRAINT `django_celery_beat_periodictask_chk_2` CHECK ((`priority` >= 0)),
  CONSTRAINT `django_celery_beat_periodictask_chk_3` CHECK ((`expire_seconds` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictask`
--

LOCK TABLES `django_celery_beat_periodictask` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictask` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_periodictask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictasks`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_periodictasks` (
  `ident` smallint NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictasks`
--

LOCK TABLES `django_celery_beat_periodictasks` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_solarschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_solarschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_solarschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event` varchar(24) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq` (`event`,`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_solarschedule`
--

LOCK TABLES `django_celery_beat_solarschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(33,'capstone','certificate'),(14,'capstone','chatmessage'),(25,'capstone','comment'),(9,'capstone','feedback'),(11,'capstone','jobapplication'),(10,'capstone','joblisting'),(12,'capstone','menteeactivity'),(17,'capstone','mentorprofile'),(13,'capstone','mentorshiprequest'),(15,'capstone','message'),(23,'capstone','notification'),(16,'capstone','participantprofile'),(18,'capstone','progress'),(19,'capstone','question'),(20,'capstone','rating'),(8,'capstone','resource'),(21,'capstone','savedjob'),(22,'capstone','session'),(26,'capstone','thread'),(7,'capstone','user'),(24,'capstone','vote'),(5,'contenttypes','contenttype'),(32,'django_celery_beat','clockedschedule'),(27,'django_celery_beat','crontabschedule'),(28,'django_celery_beat','intervalschedule'),(29,'django_celery_beat','periodictask'),(30,'django_celery_beat','periodictasks'),(31,'django_celery_beat','solarschedule'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (80,'contenttypes','0001_initial','2025-02-13 10:25:34.559806'),(81,'contenttypes','0002_remove_content_type_name','2025-02-13 10:28:55.472908'),(82,'auth','0001_initial','2025-02-13 10:28:55.486506'),(83,'auth','0002_alter_permission_name_max_length','2025-02-13 10:28:55.582193'),(84,'auth','0003_alter_user_email_max_length','2025-02-13 10:28:55.589201'),(85,'auth','0004_alter_user_username_opts','2025-02-13 10:28:55.599844'),(86,'auth','0005_alter_user_last_login_null','2025-02-13 10:28:55.611258'),(87,'auth','0006_require_contenttypes_0002','2025-02-13 10:28:55.617280'),(88,'auth','0007_alter_validators_add_error_messages','2025-02-13 10:28:55.627945'),(89,'auth','0008_alter_user_username_max_length','2025-02-13 10:28:55.642564'),(90,'auth','0009_alter_user_last_name_max_length','2025-02-13 10:28:55.650999'),(91,'auth','0010_alter_group_name_max_length','2025-02-13 10:28:55.735600'),(92,'auth','0011_update_proxy_permissions','2025-02-13 10:28:55.745205'),(93,'auth','0012_alter_user_first_name_max_length','2025-02-13 10:28:55.752888');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('246auii2qjpdgmks5kb68xi5x4mwfbpp','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1tg37Q:PVguShGikOj9rSy4usM_s9e-Twfra1M76tqTLA-LDDU','2025-02-20 14:44:40.046874'),('69avazr57yvht1u4296o5q7zp1n8igec','.eJxVjDsOwjAQBe_iGln-xJ9Q0ucM1q53wQFkS3FSIe4OkVJA-2bmvUSCbS1p67ykmcRZaC1OvyNCfnDdCd2h3prMra7LjHJX5EG7nBrx83K4fwcFevnWRlvLKkeHMUQkYygzhoEH740yELQFF1lFF5A0wJi9CleLwZBnGh2K9wf4rzf9:1thYcS:l9WU0pfOa7r3dm_M7u1MS2K37nz3rmLqMRkPLfjL9uc','2025-02-24 18:34:56.105869'),('9m16630i06hvej2gfs29t1hc8qtv4qy7','.eJxVjE0OgyAYBe_CuiEggtBl957BfH9W2wYT0VXTu1cSF-12Zt57qwH2bRr2Iusws7qqqC6_DIGekqvgB-T7omnJ2zqjrok-bdH9wvK6ne3fwQRlqmtr2AQb7UicYoeNlRgAoUXHLngkC9SIaTiITy65gxyu82Mr5AVJfb7yyDi2:1tf5I4:jUBNuk86lRSW_mi3uYZ_1Po5S2kszA7C1uO_DdYiy78','2025-02-17 22:51:40.705989'),('9w08utxar43nilezmvytrdkg25w4x6zj','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1tiDQa:Cxx72EDH4wrhk3PqRKT6E-61824e3-IOcjFdnzrt7gY','2025-02-26 14:09:24.645473'),('bqa71t3k363af45rt0ir40zgvj5bcqnr','.eJxVjDsOwjAQBe_iGlnG3zUlfc5g7a7XJIASKZ8KcXeIlALaNzPvpQpua1-2ReYyVHVRoE6_GyE_ZNxBveN4mzRP4zoPpHdFH3TR3VTleT3cv4Mel_5bE7lK2QQfq0ncmkGWFjCJ82eLkaMVStmBheiDCDBBTtYl37IIZ1DvDwJnOFc:1thr80:98cYx-t5xTIQI0tddYKD_s8nla4K0MgSDUt-GhIRIvY','2025-02-25 14:20:44.954600'),('c40jefxydal52hea1n4fj7y7ztiji7tl','e30:1tfphk:4847OApUa20QaIzxBpq2S2SnfQ8TMsbEmDdxqwRd0WQ','2025-02-20 00:25:16.323803'),('deo40y2qpuogtmfpwsmty2d6472nmt5w','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1tfEkz:YdZWNVYXNtMKRQTvDMYj3CVze0mvSdVjLVl9xyPiRHQ','2025-02-18 08:58:09.285089'),('ej17ar24xozkaaza8nlzfcb51sbtxb5a','.eJxVjDsOwjAQBe_iGlnG3zUlfc5g7a7XJIASKZ8KcXeIlALaNzPvpQpua1-2ReYyVHVRoE6_GyE_ZNxBveN4mzRP4zoPpHdFH3TR3VTleT3cv4Mel_5bE7lK2QQfq0ncmkGWFjCJ82eLkaMVStmBheiDCDBBTtYl37IIZ1DvDwJnOFc:1tfhZ2:GnDdZHrvUoXscxS_umAujnv5XBO9BYXZc3b3s4mG8OY','2025-02-19 15:43:44.300513'),('fx48dlllwk5dugwhqw974e0qx55r17zz','.eJxVjDsOwjAQBe_iGln-xJ9Q0ucM1q53wQFkS3FSIe4OkVJA-2bmvUSCbS1p67ykmcRZaC1OvyNCfnDdCd2h3prMra7LjHJX5EG7nBrx83K4fwcFevnWRlvLKkeHMUQkYygzhoEH740yELQFF1lFF5A0wJi9CleLwZBnGh2K9wf4rzf9:1tgTeH:_b16kr3AH7ZcuYwLk9vtSVJ9NIPDu4BsWhuigfrqqJ4','2025-02-21 19:04:21.734612'),('i4vfm4cjxpbxwxkb0s696v5yrhzx673h','.eJxVjE0OgyAYBe_CuiEggtBl957BfH9W2wYT0VXTu1cSF-12Zt57qwH2bRr2Iusws7qqqC6_DIGekqvgB-T7omnJ2zqjrok-bdH9wvK6ne3fwQRlqmtr2AQb7UicYoeNlRgAoUXHLngkC9SIaTiITy65gxyu82Mr5AVJfb7yyDi2:1tel99:BWmRiGbHHGBxmjmDFo2ABLNQkto1GpVWw1MopXDb9EE','2025-02-17 01:21:07.453206'),('okejyjguuzfpfmckopm502io1nu18qrx','e30:1tfpga:CzrQ2WcyXKmllEL12soh7NgjcpJVXeDvWmESYhhGvUA','2025-02-20 00:24:04.714106'),('p5d8yqfja5xrthuzp9kw21oil47u755u','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1tfTOE:BmVkinxxY2ODZnVeU_7PD1DggyYOBEYtCQUEJ8qeW1g','2025-02-19 00:35:38.816192'),('qmo279khkk1joqif7r3vd2gmxthj3g28','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1tejSG:YnmMpNfatMXf8eGOmHgMdA_wQswq0UTHMEw5lld3Sek','2025-02-16 23:32:44.005143'),('raiinu9getx62pvnl9v4mhxnuyhkqr0g','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1tgBnT:_vGLkp0OsC_RNdTecOJ_fQpq11GXKzNfOJZBIrwfoDA','2025-02-21 00:00:39.673078'),('rpa0jz731tfwr52t3uqvtqpwous2p66x','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1teF3W:OA90GBljwYI54Ihr4gIK8lBJ4boHiFlr3UqWv0u36m8','2025-02-15 15:05:10.501101'),('udbd5s65rogg7vm5hpny0ycu2x7yoj8o','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1teEyp:b0M6TC2BZqhZQfAmrm7HLf9uHJ4UyP1d85Krfy1VaxQ','2025-02-15 15:00:19.437402'),('ujxpnet8y2bvirpks4rfh7dzghj7ryhk','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1tiMKv:ZYeQjYow9uw3qV_MKmdGNTauc4mEl1MW9fnzjAazyD8','2025-02-26 23:40:09.386624'),('wdfaueqvfuocl1zn90dbpsq01j5fhxc9','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1tf7VR:5x_z5ZSCIYRjsItpeiNWha4Sm7gfoHj7nNYPK3-XJmQ','2025-02-18 01:13:37.589596'),('wxibxfjb4nhts8e591on300zrk99qqz7','.eJxVjMEOwiAQBf-FsyFAFwSP3v0GAuwiVQNJaU_Gf5cmPej1zcx7Mx-2tfit0-JnZBfm2Ol3iyE9qe4AH6HeG0-trssc-a7wg3Z-a0iv6-H-HZTQy6gDJItCkTwrCTmBBhQIKTvpaLITaEI3FAHW2jhup6gRsonaGKtGxD5f4jw3gw:1tfq71:8Tr5eQRPKco0xG_-V4khNWxE3G2_TulRk6G6DmJp854','2025-02-20 00:51:23.949988'),('xps6a813gv9859r22th4rjdwyosebc80','.eJxVjDsOwjAQBe_iGlnG3zUlfc5g7a7XJIASKZ8KcXeIlALaNzPvpQpua1-2ReYyVHVRoE6_GyE_ZNxBveN4mzRP4zoPpHdFH3TR3VTleT3cv4Mel_5bE7lK2QQfq0ncmkGWFjCJ82eLkaMVStmBheiDCDBBTtYl37IIZ1DvDwJnOFc:1thxr5:L-DHwyvkevTZF056ye7jDxnp5lSmUAta37EJaPL6Rbc','2025-02-25 21:31:43.550179'),('y1x3f0k6xrs16sxetpat43xj7mo6w9cg','e30:1tfpdg:p7IUgwQ_zSpVm4Gvc7O3zhNgi-IAoarpOzwjVozDWvI','2025-02-20 00:21:04.860712');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-13 12:32:05
