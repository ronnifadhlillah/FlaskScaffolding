-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.14-MariaDB

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
-- Table structure for table `mock_data`
--

DROP TABLE IF EXISTS `mock_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mock_data` (
  `id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `ip_address` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mock_data`
--

LOCK TABLES `mock_data` WRITE;
/*!40000 ALTER TABLE `mock_data` DISABLE KEYS */;
INSERT INTO `mock_data` VALUES (98,'Mario','Pinyon','mpinyon2p@reverbnation.com','Male','150.30.83.71'),(1,'Laureen','Aguirre','laguirre0@ow.ly','Bigender','223.191.111.109'),(2,'Hortensia','Filipson','hfilipson1@skype.com','Female','249.251.125.202'),(3,'Shena','Greenham','sgreenham2@theguardian.com','Male','36.176.32.69'),(4,'Candy','Rainbow','crainbow3@feedburner.com','Genderqueer','156.252.179.66'),(5,'Ralph','Jeffcoate','rjeffcoate4@pagesperso-orange.fr','Genderqueer','218.61.125.47'),(6,'Dre','Gozney','dgozney5@prweb.com','Bigender','75.9.166.189'),(7,'Bron','Balassi','bbalassi6@dmoz.org','Male','119.69.223.245'),(8,'Grier','Gammidge','ggammidge7@adobe.com','Agender','34.153.42.75'),(9,'Cordie','Moran','cmoran8@amazon.de','Agender','2.111.15.232'),(10,'Philip','Elderfield','pelderfield9@time.com','Non-binary','111.247.8.207'),(11,'Ingaberg','Ashworth','iashwortha@slashdot.org','Male','172.19.131.157'),(12,'Franciskus','Simpkin','fsimpkinb@networksolutions.com','Male','2.126.85.222'),(13,'Anette','Turpey','aturpeyc@people.com.cn','Polygender','96.253.148.184'),(14,'Temp','Michin','tmichind@auda.org.au','Agender','151.141.182.158'),(15,'Kelwin','Sarginson','ksarginsone@t.co','Genderqueer','221.251.217.43'),(16,'Carolynn','Tanzig','ctanzigf@a8.net','Genderfluid','100.112.98.38'),(17,'Brad','Holberry','bholberryg@microsoft.com','Genderfluid','167.180.107.231'),(18,'Kalil','Stanyon','kstanyonh@wix.com','Male','178.39.43.220'),(19,'Mina','Kohrsen','mkohrseni@answers.com','Female','210.178.114.162'),(20,'Flory','Yacob','fyacobj@deliciousdays.com','Male','222.161.27.23'),(21,'Arlyne','Yewdale','ayewdalek@blinklist.com','Bigender','218.180.172.159'),(22,'Erina','Couper','ecouperl@webs.com','Genderqueer','154.195.200.50'),(23,'Zerk','Eliasson','zeliassonm@1688.com','Bigender','206.72.134.35'),(24,'Ray','Saenz','rsaenzn@bizjournals.com','Genderfluid','8.244.80.54'),(25,'Arel','Tremmil','atremmilo@phpbb.com','Non-binary','107.85.29.38'),(26,'Dolph','Karpychev','dkarpychevp@canalblog.com','Agender','35.95.155.61'),(27,'Kurtis','Greenstreet','kgreenstreetq@cargocollective.com','Female','19.52.243.129'),(28,'Odetta','Galiford','ogalifordr@fc2.com','Non-binary','171.30.209.81'),(29,'Nikkie','Underwood','nunderwoods@google.pl','Non-binary','61.5.64.11'),(30,'Bobby','Jelks','bjelkst@seesaa.net','Bigender','231.101.28.118'),(31,'Trev','Lancaster','tlancasteru@godaddy.com','Polygender','231.146.38.166'),(32,'Berti','Mingay','bmingayv@netscape.com','Non-binary','220.164.184.98'),(33,'Alicia','Lathwood','alathwoodw@fda.gov','Female','53.188.38.160'),(34,'Larisa','Alejandro','lalejandrox@earthlink.net','Male','71.205.9.14'),(35,'Veda','Guyon','vguyony@craigslist.org','Bigender','228.188.107.75'),(36,'Gaston','Izen','gizenz@over-blog.com','Non-binary','192.231.63.209'),(37,'Jesselyn','Mafham','jmafham10@parallels.com','Polygender','40.199.230.56'),(38,'Worden','Averay','waveray11@yellowpages.com','Genderqueer','133.217.190.166'),(39,'Sterne','Dragonette','sdragonette12@wsj.com','Agender','172.88.159.52'),(40,'Mathilda','Donavan','mdonavan13@mapquest.com','Genderqueer','97.223.5.159'),(41,'Vina','Wem','vwem14@vk.com','Bigender','225.87.150.237'),(42,'Carmel','Lashmar','clashmar15@artisteer.com','Female','138.50.132.161'),(43,'Elvera','Esposita','eesposita16@cornell.edu','Male','233.222.245.140'),(44,'Alisander','Garman','agarman17@infoseek.co.jp','Bigender','107.38.98.1'),(45,'Corrina','de Bullion','cdebullion18@salon.com','Genderqueer','52.76.9.52'),(46,'Tammie','Franies','tfranies19@elegantthemes.com','Female','180.248.78.178'),(47,'Gaven','Cherrie','gcherrie1a@redcross.org','Agender','220.36.40.233'),(48,'Vivianna','Hitchens','vhitchens1b@ft.com','Bigender','54.59.136.64'),(49,'Kelsey','Lapree','klapree1c@upenn.edu','Genderfluid','114.110.181.217'),(50,'Emelyne','Pawel','epawel1d@miibeian.gov.cn','Male','218.88.67.193'),(51,'Stormie','Hrus','shrus1e@opera.com','Genderqueer','89.206.208.212'),(52,'Raymond','Luesley','rluesley1f@privacy.gov.au','Agender','57.220.135.80'),(53,'Roldan','Lemmen','rlemmen1g@disqus.com','Agender','167.240.111.89'),(54,'Fredek','Casarili','fcasarili1h@cnn.com','Male','33.109.100.72'),(55,'Erina','Lowen','elowen1i@t.co','Bigender','24.130.123.233'),(56,'Granville','Biernat','gbiernat1j@alexa.com','Non-binary','162.91.69.109'),(57,'Robinetta','Sprowles','rsprowles1k@mediafire.com','Polygender','52.170.99.134'),(58,'Vin','Eyeington','veyeington1l@cdc.gov','Genderqueer','182.180.176.30'),(59,'Nertie','Lacasa','nlacasa1m@last.fm','Bigender','22.13.19.97'),(60,'Jerad','Lyosik','jlyosik1n@yahoo.co.jp','Polygender','144.246.185.55'),(61,'Anastasia','Cornfield','acornfield1o@tmall.com','Polygender','85.231.141.184'),(62,'Rickey','Saller','rsaller1p@plala.or.jp','Agender','36.25.47.130'),(63,'Alexine','Yes','ayes1q@theguardian.com','Non-binary','141.147.221.140'),(64,'Yetty','Caldwell','ycaldwell1r@vinaora.com','Non-binary','143.123.87.12'),(65,'Trueman','Waryk','twaryk1s@newyorker.com','Polygender','184.215.217.235'),(66,'Mariette','Giraudot','mgiraudot1t@nyu.edu','Genderfluid','114.97.85.113'),(67,'Milo','Widdison','mwiddison1u@diigo.com','Bigender','30.67.166.190'),(68,'Willow','Biles','wbiles1v@icio.us','Genderqueer','116.253.176.192'),(69,'Sheela','Orehead','sorehead1w@blinklist.com','Polygender','228.116.159.215'),(70,'Johnna','Havoc','jhavoc1x@google.cn','Female','187.103.170.74'),(71,'Sanson','Boorn','sboorn1y@topsy.com','Genderfluid','22.15.100.11'),(72,'Salmon','Dellenbroker','sdellenbroker1z@ezinearticles.com','Male','119.182.206.46'),(73,'Elke','Bern','ebern20@amazonaws.com','Male','81.50.164.2'),(74,'Hillary','Betun','hbetun21@npr.org','Genderfluid','162.116.190.194'),(75,'Ciro','Prantl','cprantl22@diigo.com','Genderfluid','176.153.219.65'),(76,'Patrica','Heyns','pheyns23@shutterfly.com','Bigender','233.38.48.43'),(77,'Nicky','Banks','nbanks24@newyorker.com','Polygender','107.185.243.208'),(78,'Erna','Soreau','esoreau25@devhub.com','Non-binary','170.118.252.254'),(79,'Polly','Garnett','pgarnett26@tripod.com','Agender','242.191.44.50'),(80,'Koo','Okker','kokker27@tripod.com','Non-binary','40.176.128.177'),(81,'Berkeley','Heinz','bheinz28@squarespace.com','Bigender','66.62.142.238'),(82,'Elvyn','Antczak','eantczak29@twitpic.com','Agender','127.121.221.55'),(83,'Horace','Adamovitch','hadamovitch2a@dailymotion.com','Agender','1.180.244.231'),(84,'Pamella','Hanstock','phanstock2b@indiegogo.com','Bigender','153.136.179.108'),(85,'Konstantine','Playfair','kplayfair2c@dell.com','Genderfluid','203.89.125.60'),(86,'Clerkclaude','Runnalls','crunnalls2d@csmonitor.com','Non-binary','57.124.240.104'),(87,'Selig','Grayham','sgrayham2e@cbsnews.com','Non-binary','201.102.15.45'),(88,'Latrena','Wrought','lwrought2f@feedburner.com','Male','40.29.171.94'),(89,'Ulberto','Hartfield','uhartfield2g@ebay.co.uk','Polygender','42.183.163.219'),(90,'Wendi','Mayhow','wmayhow2h@psu.edu','Female','125.6.3.248'),(91,'Torin','Pavek','tpavek2i@blinklist.com','Female','54.116.28.186'),(92,'Neale','Kunath','nkunath2j@mapy.cz','Genderqueer','204.69.193.73'),(93,'Karalynn','Swateridge','kswateridge2k@acquirethisname.com','Non-binary','131.227.54.133'),(94,'Ivory','Sarney','isarney2l@seesaa.net','Non-binary','86.75.81.157'),(95,'Kaja','Davidovitz','kdavidovitz2m@salon.com','Bigender','163.218.125.249'),(96,'Gigi','Cornwall','gcornwall2n@woothemes.com','Non-binary','61.5.178.78'),(97,'Dorisa','Alecock','dalecock2o@moonfruit.com','Agender','125.192.141.184'),(98,'Mario','Pinyon','mpinyon2p@reverbnation.com','Male','150.30.83.71');
/*!40000 ALTER TABLE `mock_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-18  0:23:22
