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
-- Table structure for table `support`
--

DROP TABLE IF EXISTS `support`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `support` (
  `support_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `issue` varchar(1000) DEFAULT NULL,
  `issue_date` date DEFAULT NULL,
  PRIMARY KEY (`support_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `support_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `support`
--

LOCK TABLES `support` WRITE;
/*!40000 ALTER TABLE `support` DISABLE KEYS */;
INSERT INTO `support` VALUES (1,269,'Ihe colour of phone does not match with the one I ordered','2021-10-10'),(2,450,'I am not able to add products to my cart','2022-11-12'),(3,73,'The iron I ordered is not heating up properly','2022-01-27'),(4,90,'The lid of the blender was broken','2022-02-19'),(5,90,'The lid of the blender was broken','2022-02-27'),(6,123,'Laptop is not turning on','2022-02-25'),(7,234,'Earphone not working','2022-02-23'),(8,345,'I am not able to place order','2022-02-23'),(9,456,'I have not recieved my order which was meant to be delivered yesterday','2022-02-27'),(10,678,'Wrong item was sent','2022-02-25'),(11,890,'Quality not adequate','2022-02-18'),(12,901,'The packaging of the product was already opened.','2022-02-15'),(13,433,'Unavailable or out of stock product','2022-02-10'),(14,167,'Money not refunded','2022-02-05'),(15,298,'The toothpaste was expired','2022-01-26'),(16,888,'Billing Issues','2022-01-23'),(17,40,'The fruits were not fresh','2022-01-20'),(18,567,'I am unable to avail the displayed offer','2022-01-19'),(19,786,'The lid of the blender was broken','2022-01-19'),(20,99,'I am unable to avail the displayed offer','2022-01-13'),(21,200,'Unavailable or out of stock product','2022-01-13'),(22,100,'I am unable to avail the displayed offer','2022-01-10'),(23,300,'unable to log in on the app','2022-01-10'),(24,444,'Prices Are Too High','2020-01-10'),(25,44,'Not Happy with Buynget Services','2022-05-01'),(26,66,'Not Happy with Buynget Services','2022-05-01'),(27,90,'Not Happy with Buynget Services','2022-05-01'),(28,46,'Not Happy with Buynget Services','2022-05-01'),(29,900,'Not Happy with Buynget Services','2022-05-01'),(30,69,'Not Happy with Buynget Services','2022-05-01'),(31,67,'Not Happy with Buynget Services','2022-05-01'),(32,123,'Not Happy with Buynget Services','2022-05-01'),(33,234,'Not Happy with Buynget Services','2022-05-01'),(34,771,'Not Happy with Buynget Services','2022-05-01'),(35,89,'Not Happy with Buynget Services','2022-05-01'),(36,50,'Not Happy with Buynget Services','2022-05-01'),(37,403,'Not Happy with Buynget Services','2022-05-01'),(38,654,'Not Happy with Buynget Services','2022-05-01'),(39,299,'Not Happy with Buynget Services','2022-05-01'),(40,399,'Not Happy with Buynget Services','2022-05-01'),(41,666,'Not Happy with Buynget Services','2022-05-01');
/*!40000 ALTER TABLE `support` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-01  2:47:40
