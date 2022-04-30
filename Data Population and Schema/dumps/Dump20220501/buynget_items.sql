-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: buynget
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(50) NOT NULL,
  `item_type` varchar(20) NOT NULL,
  `quantity` int DEFAULT NULL,
  `cost_price` float NOT NULL,
  `selling_price` float NOT NULL,
  PRIMARY KEY (`item_id`),
  CONSTRAINT `items_chk_1` CHECK ((`quantity` > 0)),
  CONSTRAINT `items_chk_2` CHECK ((`cost_price` > 0)),
  CONSTRAINT `items_chk_3` CHECK ((`selling_price` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,'apple','Grocery',500,0.37,0.4),(2,'banana','Grocery',165,0.053,0.066),(3,'pear','Grocery',254,0.28,0.33),(4,'figs','Grocery',120,0.092,0.13),(5,'onion','Grocery',86,0.079,0.092),(6,'strawberry','Grocery',370,0.066,0.092),(7,'pineapple','Grocery',399,0.59,0.66),(8,'watermelon','Grocery',115,0.92,0.99),(9,'pomegranate','Grocery',229,0.53,0.61),(10,'muskmelon','Grocery',655,0.78,0.79),(11,'guava','Grocery',314,0.11,0.13),(12,'orange','Grocery',470,0.26,0.29),(13,'potato','Grocery',934,0.04,0.053),(14,'cauliflower','Grocery',427,0.62,0.66),(15,'corn','Grocery',599,0.2,0.21),(16,'pumpkin','Grocery',429,1.02,1.06),(17,'papaya','Grocery',173,0.58,0.59),(18,'cabbage','Grocery',350,0.91,0.92),(19,'coconut','Grocery',584,0.16,0.2),(20,'broccoli','Grocery',150,0.4,0.46),(21,'tomato','Grocery',785,0.026,0.066),(22,'ginger','Grocery',100,0.092,0.13),(23,'lemon','Grocery',85,0.066,0.092),(24,'kiwi','Grocery',170,0.34,0.4),(25,'coriander','Grocery',511,0.053,0.066),(26,'spinach','Grocery',420,0.04,0.092),(27,'lettuce','Grocery',313,0.28,0.33),(28,'mint','Grocery',260,0.066,0.079),(29,'cucumber','Grocery',310,0.053,0.066),(30,'garlic','Grocery',800,0.26,0.36),(31,'brinjal','Grocery',587,0.13,0.15),(32,'grapes','Grocery',770,0.48,0.49),(33,'chikoo','Grocery',487,0.026,0.066),(34,'fenugreek','Grocery',360,0.11,0.16),(35,'avocado','Grocery',113,1.58,1.72),(36,'olive oil','Grocery',20,5,9),(37,'canned milk','Grocery',16,0.94,1.38),(38,'brown sugar','Grocery',29,2,4.7),(39,'sugar','Grocery',39,1.54,4),(40,'instant noodles','Grocery',57,2,4),(41,'cherries','Grocery',78,2.54,3.66),(42,'mobile','Electronics',700,120,200),(43,'air conditioner','Electronics',127,450,550),(44,'television','Electronics',100,280,390),(45,'beard trimmer','Electronics',177,50,69),(46,'Body trimmer','Electronics',200,12,19),(47,'LED bulb','Electronics',180,3,5),(48,'extension cord','Electronics',70,4,6),(49,'earphones','Electronics',479,7,9),(50,'power bank','Electronics',300,18,24),(51,'wifi router','Electronics',78,38,60),(52,'wrist watch','Electronics',700,70,99),(53,'wall clock','Electronics',181,45,70),(54,'fitbit','Electronics',1000,55,70),(55,'headphones','Electronics',380,180,279),(56,'apple air pods','Electronics',300,100,200),(57,'laptop','Electronics',230,350,460),(58,'gaming mouse','Electronics',500,27,42),(59,'keyboard','Electronics',379,15,28),(60,'table lamp','Electronics',100,9,15),(61,'flashlight','Electronics',205,9,17),(62,'electrical toothbrush','Electronics',100,22,39),(63,'washing Machine','Electronics',141,230,312),(64,'refrigerator','Electronics',125,180,240),(65,'air purifier','Electronics',74,100,150),(66,'toaster','Electronics',75,25,40),(67,'hair straightener','Electronics',83,25,40),(68,'blender','Electronics',134,40,65),(69,'inverter battery','Electronics',87,90,140),(70,'projector','Electronics',50,1500,2000),(71,'microwave','Electronics',89,50,70),(72,'iron','Electronics',40,20,30),(73,'heater','Electronics',37,29,32),(74,'microphone','Electronics',33,10,15),(75,'tooth-paste','Daily care',986,7,9),(76,'tooth-brush','Daily care',1500,9,15),(77,'diapers','Daily care',690,50,60),(78,'facewash','Daily care',300,11,15),(79,'perfume','Daily care',154,40,45),(80,'soap','Daily care',900,1,2),(81,'hairspray','Daily care',106,16,20),(82,'hair shampoo','Daily care',210,6,9),(83,'dental floss','Daily care',101,7,10),(84,'face mask','Daily care',3000,4,6),(85,'sanitizer','Daily care',984,8,14),(86,'liquid handwash','Daily care',234,3,5),(87,'lotion','Daily care',182,6,8),(88,'nail clippers','Daily Care',78,5,7),(89,'moisturizer','Daily Care',181,20,27),(90,'foundation','Daily Care',60,15,20),(91,'mosquito repellent','Daily Care',81,3,4),(92,'body wash','Daily Care',122,8,10),(93,'disinfectant liquid','Daily Care',37,10,15),(94,'disinfectant spray','Daily Care',77,11,14),(95,'lipstick','Daily Care',83,5,7),(96,'eyeliner','Daily Care',88,6,7),(97,'mascara','Daily Care',35,9,12),(98,'nail polish remover','Daily Care',90,16,24),(99,'nail polish','Daily Care',163,20,30),(100,'eye lubricant','Daily Care',50,7,10),(101,'sunscreen lotion','Daily Care',57,4,5),(102,'hair serum','Daily Care',99,22,35),(103,'hair oil','Daily Care',90,7,8),(104,'tooth picks','Daily Care',150,2,3);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-01  2:41:17
