/*
SQLyog Enterprise - MySQL GUI v8.02 RC
MySQL - 5.5.5-10.3.16-MariaDB : Database - courier
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`courier` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `courier`;

/*Table structure for table `admin_data` */

DROP TABLE IF EXISTS `admin_data`;

CREATE TABLE `admin_data` (
  `name` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admin_data` */

insert  into `admin_data`(`name`,`address`,`contact`,`email`) values ('Payal Lakhotia','35,New Grain Mandi','5246437894','p@gmail.com');

/*Table structure for table `agency_data` */

DROP TABLE IF EXISTS `agency_data`;

CREATE TABLE `agency_data` (
  `agency_name` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `city_name` varchar(100) DEFAULT NULL,
  `state_name` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `agency_data` */

insert  into `agency_data`(`agency_name`,`address`,`city_name`,`state_name`,`contact`,`email`) values ('Center01','71 gopal vihar 2 police line kota','kota','Rajasthan','0744-2331984','center01@gmail.com'),('Center02','51,New Colony4,Bulandshahr','Bulandshahr','Uttar Pradesh','7976472851','center02@gmail.com'),('center03','322,Mahaveer Colony,Bhiwadi','Bhiwadi','Haryana','7976472851','center03@gmail.com');

/*Table structure for table `agency_track` */

DROP TABLE IF EXISTS `agency_track`;

CREATE TABLE `agency_track` (
  `con_no` int(11) NOT NULL,
  `center_name` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`con_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `agency_track` */

/*Table structure for table `bill` */

DROP TABLE IF EXISTS `bill`;

CREATE TABLE `bill` (
  `con_no` int(11) NOT NULL,
  `agency` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `sender_name` varchar(100) DEFAULT NULL,
  `sender_address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `tax` float DEFAULT NULL,
  PRIMARY KEY (`con_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `bill` */

insert  into `bill`(`con_no`,`agency`,`date`,`sender_name`,`sender_address`,`contact`,`weight`,`price`,`tax`) values (8,'Center01','2022-05-03','gaurav Bhardwaj','71,Gopal Vihar II ( 324001)','8949336757',80,300,55.85),(11,'Center02','2022-05-13','Suresh Sharma','71 Khanoda  Bulandshahr(203001)','8949336752',40,250,85),(14,'Center02','2022-05-14','Shikha Singh','322,Mahaveer Colony,Bhiwadi(235007)','4513461842',10,250,50);

/*Table structure for table `booking_data` */

DROP TABLE IF EXISTS `booking_data`;

CREATE TABLE `booking_data` (
  `con_no` int(11) NOT NULL AUTO_INCREMENT,
  `booked_at` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `from_city` varchar(100) DEFAULT NULL,
  `state_name_1` varchar(100) DEFAULT NULL,
  `to_city` varchar(100) DEFAULT NULL,
  `sender_name` varchar(100) DEFAULT NULL,
  `sender_address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `receiver_name` varchar(100) DEFAULT NULL,
  `receiver_address` varchar(100) DEFAULT NULL,
  `receiver_contact` varchar(100) DEFAULT NULL,
  `weight` bigint(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `em_center` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`con_no`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `booking_data` */

insert  into `booking_data`(`con_no`,`booked_at`,`date`,`state`,`from_city`,`state_name_1`,`to_city`,`sender_name`,`sender_address`,`contact`,`receiver_name`,`receiver_address`,`receiver_contact`,`weight`,`email`,`em_center`) values (8,'center01','2022-05-03','Rajasthan','kota','Madhya Pradesh','Gadarwada','Gaurav Bhardwaj','71,Gopal Vihar II ( 324001)','8949336757','Nalin Sharma','C3-602 tower, narmada vihar NTPC Gadarwada colony 487770 ','8078667712',80,'center01@gmail.com','center02@gmail.com'),(11,'center02','2022-05-13','Uttar Pradesh','Bulandshahr','Rajasthan','Kota','Suresh Sharma','71 Khanoda  Bulandshahr(203001)','8949336752','Om Prakash Sharma','71 gopal Vihar II (324001 )','8949336757',40,'center02@gmail.com',NULL),(14,'center03','2022-05-14','Haryana','Bhiwadi','Rajasthan','Kota','Shikha Singh','322,Mahaveer Colony,Bhiwadi(235007)','4513461842','Payal Lakhotia','35,New Grain Mandi,kota(324007)','3246165462',10,'center03@gmail.com','center02@gmail.com'),(17,'center01','2022-05-19','Rajasthan','Kota','Uttar Pradesh','Meerut','Suman','322,Pratap Nagar,Dadabari(324005)','8949336755','Rohan','325,R.K.Nagar,Meerut(852753)','8527539516',8,'center01@gmail.com','center03@gmail.com');

/*Table structure for table `login_data` */

DROP TABLE IF EXISTS `login_data`;

CREATE TABLE `login_data` (
  `email` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login_data` */

insert  into `login_data`(`email`,`password`,`usertype`) values ('center01@gmail.com','c01','agency'),('center02@gmail.com','c02','agency'),('center03@gmail.com','c03','agency'),('p@gmail.com','203','admin');

/*Table structure for table `tracking` */

DROP TABLE IF EXISTS `tracking`;

CREATE TABLE `tracking` (
  `con_no` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `office` varchar(100) DEFAULT NULL,
  `event` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tracking` */

insert  into `tracking`(`con_no`,`date`,`time`,`office`,`event`) values (8,'2022-05-03','05:11','kota','Ready To Dispatch'),(11,'2022-05-13','12:05','Bulandshahr HO','Ready To Dispatch'),(14,'2022-05-14','11:03','Bhiwadi HO','Ready To Dispatch'),(17,'2022-05-19','12:00','kota HO','Dispatched'),(17,'2022-05-19','14:47','Meerut HO','Received');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
