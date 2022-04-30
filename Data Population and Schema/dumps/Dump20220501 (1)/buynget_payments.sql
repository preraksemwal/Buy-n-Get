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
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `mode` varchar(20) NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `sellers` (`customer_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,2,'NetBanking',100),(2,2,'NetBanking',37),(3,7,'NetBanking',24),(4,18,'NetBanking',34),(5,19,'NetBanking',26),(6,3,'NetBanking',55),(7,6,'NetBanking',40),(8,17,'NetBanking',55),(9,7,'NetBanking',200),(10,4,'NetBanking',100),(11,3,'UPI',70),(12,5,'UPI',140),(13,2,'UPI',500),(14,13,'UPI',500),(15,15,'UPI',200),(16,20,'UPI',50),(17,11,'UPI',237),(18,17,'UPI',315),(19,11,'UPI',300),(20,11,'UPI',140),(21,12,'UPI',315),(22,6,'Credit-Card',212),(23,17,'Credit-Card',165),(24,9,'Credit-Card',60),(25,9,'Credit-Card',30),(26,10,'Credit-Card',1200),(27,10,'Credit-Card',9000),(28,9,'Credit-Card',900),(29,4,'Credit-Card',900),(30,1,'Credit-Card',1800),(31,8,'Debit-Card',300),(32,17,'Debit-Card',400),(33,8,'Debit-Card',90),(34,19,'Debit-Card',700),(35,4,'Debit-Card',63),(36,4,'Debit-Card',900),(37,5,'Debit-Card',70),(38,15,'Debit-Card',1000),(39,5,'Debit-Card',500),(40,16,'Debit-Card',400);
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-01  2:47:01
