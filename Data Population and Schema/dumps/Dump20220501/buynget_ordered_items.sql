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
-- Table structure for table `ordered_items`
--

DROP TABLE IF EXISTS `ordered_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordered_items` (
  `order_id` int NOT NULL,
  `item_id` int NOT NULL,
  `quantity` int DEFAULT NULL,
  KEY `order_id` (`order_id`),
  KEY `item_id` (`item_id`),
  CONSTRAINT `ordered_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE,
  CONSTRAINT `ordered_items_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE,
  CONSTRAINT `ordered_items_chk_1` CHECK ((`quantity` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordered_items`
--

LOCK TABLES `ordered_items` WRITE;
/*!40000 ALTER TABLE `ordered_items` DISABLE KEYS */;
INSERT INTO `ordered_items` VALUES (1,3,6),(1,5,11),(2,5,3),(2,7,8),(3,7,3),(3,9,8),(4,9,8),(4,11,13),(5,11,7),(5,13,12),(6,13,4),(6,15,9),(7,15,4),(7,17,9),(8,17,7),(8,19,12),(9,19,4),(9,21,9),(10,21,6),(10,23,11),(11,23,4),(11,25,9),(12,25,10),(12,27,15),(13,27,2),(13,29,7),(14,29,3),(14,31,8),(15,31,5),(15,33,10),(16,33,3),(16,35,8),(17,35,9),(17,37,14),(18,37,2),(18,39,7),(19,39,9),(19,41,14),(20,41,8),(20,43,13),(21,43,10),(21,45,15),(22,45,8),(22,47,13),(23,47,7),(23,49,12),(24,49,9),(24,51,14),(25,51,8),(25,53,13),(26,53,6),(26,55,11),(27,55,9),(27,57,14),(28,57,6),(28,59,11),(29,59,10),(29,61,15),(30,61,10),(30,63,15),(31,63,2),(31,65,7),(32,65,7),(32,67,12),(33,67,5),(33,69,10),(34,69,3),(34,71,8),(35,71,3),(35,73,8),(36,73,7),(36,75,12),(37,75,2),(37,77,7),(38,77,3),(38,79,8),(39,79,7),(39,81,12),(40,81,2),(40,83,7),(41,83,5),(41,85,10),(42,85,6),(42,87,11),(43,87,6),(43,89,11),(44,89,8),(44,91,13),(45,91,6),(45,93,11),(46,93,2),(46,95,7),(47,95,10),(47,97,15),(48,97,4),(48,99,9),(49,99,7),(49,101,12);
/*!40000 ALTER TABLE `ordered_items` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `stock_updation` AFTER INSERT ON `ordered_items` FOR EACH ROW BEGIN
   DECLARE id int;
   DECLARE q int;
   SET id = NEW.item_id;	
   SET q = NEW.quantity;
   
   UPDATE items SET items.quantity = items.quantity - q where item_id = id;
   
   END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-01  2:41:15
