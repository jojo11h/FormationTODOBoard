/*Create schema and use it !*/
CREATE SCHEMA `todoboard_test` ;
USE todoboard_test;

-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: todoboard
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `configurations`
--

DROP TABLE IF EXISTS `configurations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `configurations` (
  `Id` varchar(36) NOT NULL,
  `TodoBackgroundColor` varchar(9) NOT NULL,
  `CreationUserId` varchar(36) NOT NULL,
  `CreationDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ModificationUserId` varchar(36) NOT NULL,
  `ModificationDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`),
  KEY `FK_CONFIGURATIONS_USERS_CREATION_ID_idx` (`CreationUserId`),
  KEY `FK_CONFIGURATIONS_USERS_MODIFICATION_ID_idx` (`ModificationUserId`),
  CONSTRAINT `FK_CONFIGURATIONS_USERS_CREATION_ID` FOREIGN KEY (`CreationUserId`) REFERENCES `users` (`Id`),
  CONSTRAINT `FK_CONFIGURATIONS_USERS_MODIFICATION_ID` FOREIGN KEY (`ModificationUserId`) REFERENCES `users` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configurations`
--

LOCK TABLES `configurations` WRITE;
/*!40000 ALTER TABLE `configurations` DISABLE KEYS */;
INSERT INTO `configurations` VALUES ('27d42a49-82d4-11ee-bb27-00155d000d32','#ff00ff','3032baba-823a-11ee-ad04-00155d000d32','2023-11-14 15:04:30','3032baba-823a-11ee-ad04-00155d000d32','2023-11-14 15:04:30');
/*!40000 ALTER TABLE `configurations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `todos`
--

DROP TABLE IF EXISTS `todos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `todos` (
  `Id` varchar(36) NOT NULL,
  `Label` text NOT NULL,
  `IsProcessed` bit(1) NOT NULL,
  `CreationUserId` varchar(36) NOT NULL,
  `CreationDate` datetime NOT NULL,
  `ModificationUserId` varchar(36) NOT NULL,
  `ModificationDate` datetime NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK_USERS_CREATION_ID_idx` (`CreationUserId`),
  KEY `FK_USERS_MODIFICATION_ID_idx` (`ModificationUserId`),
  CONSTRAINT `FK_USERS_CREATION_ID` FOREIGN KEY (`CreationUserId`) REFERENCES `users` (`Id`),
  CONSTRAINT `FK_USERS_MODIFICATION_ID` FOREIGN KEY (`ModificationUserId`) REFERENCES `users` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todos`
--

LOCK TABLES `todos` WRITE;
/*!40000 ALTER TABLE `todos` DISABLE KEYS */;
INSERT INTO `todos` VALUES ('4f8a9d33-823b-11ee-ad04-00155d000d32','Tailler les rosiers chez Georgette',_binary '\0','3032baba-823a-11ee-ad04-00155d000d32','2023-11-13 16:42:54','3032baba-823a-11ee-ad04-00155d000d32','2023-11-13 16:42:54'),('85dded4d-0af8-4f2b-9029-6b55f48a8d0b','Planter des oeillets d\'inde',_binary '','3032baba-823a-11ee-ad04-00155d000d32','2023-11-14 18:36:30','3032baba-823a-11ee-ad04-00155d000d32','2023-11-14 18:36:44');
/*!40000 ALTER TABLE `todos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `Id` varchar(36) NOT NULL,
  `FirstName` text,
  `LastName` text,
  `Email` text,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('3032baba-823a-11ee-ad04-00155d000d32','Fred','Sapin','fred.sapin@nature.fr'),('3032c2c0-823a-11ee-ad04-00155d000d32','Nicole','Erable','nicole.erable@nature.fr');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-15 11:01:24
