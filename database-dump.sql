-- MySQL dump 10.13  Distrib 5.7.32, for Linux (x86_64)
--
-- Host: localhost    Database: flask_db
-- ------------------------------------------------------
-- Server version	5.7.32-0ubuntu0.18.04.1

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
-- Table structure for table `administrateur`
--

DROP TABLE IF EXISTS `administrateur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrateur` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom_admin` varchar(60) DEFAULT NULL,
  `prenom_admin` varchar(60) DEFAULT NULL,
  `sexe_admin` varchar(60) DEFAULT NULL,
  `departement_id` int(11) DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `is_superadmin` tinyint(1) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `adresse` varchar(60) DEFAULT NULL,
  `code_postal` int(11) DEFAULT NULL,
  `pays` varchar(60) DEFAULT NULL,
  `ville` varchar(60) DEFAULT NULL,
  `type` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_administrateur_email` (`email`),
  KEY `departement_id` (`departement_id`),
  KEY `ix_administrateur_nom_admin` (`nom_admin`),
  KEY `ix_administrateur_prenom_admin` (`prenom_admin`),
  KEY `ix_administrateur_sexe_admin` (`sexe_admin`),
  KEY `ix_administrateur_date_naissance` (`date_naissance`),
  CONSTRAINT `administrateur_ibfk_1` FOREIGN KEY (`departement_id`) REFERENCES `departement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrateur`
--

LOCK TABLES `administrateur` WRITE;
/*!40000 ALTER TABLE `administrateur` DISABLE KEYS */;
INSERT INTO `administrateur` VALUES (1,'admin','admin','F',1,'1989-10-10','admin@gmail.com',0,'admin','9 rue pierre legrand',75013,'FRANCE','PARIS','admin'),(2,'superadmin','superadmin','F',6,'1989-10-09','superadmin@gmail.com',1,'superadmin',NULL,NULL,NULL,NULL,'admin'),(3,'raja','lamgarmel','F',1,'1999-10-10','raja@gmail.com',0,'raja',NULL,NULL,NULL,NULL,'admin');
/*!40000 ALTER TABLE `administrateur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('4a4d3bdfd295');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `annonce`
--

DROP TABLE IF EXISTS `annonce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `annonce` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titre` varchar(200) DEFAULT NULL,
  `contenu` varchar(400) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `matiere_id` int(11) DEFAULT NULL,
  `formation_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `formation_id` (`formation_id`),
  KEY `matiere_id` (`matiere_id`),
  CONSTRAINT `annonce_ibfk_1` FOREIGN KEY (`formation_id`) REFERENCES `formation` (`id`),
  CONSTRAINT `annonce_ibfk_2` FOREIGN KEY (`matiere_id`) REFERENCES `matiere` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `annonce`
--

LOCK TABLES `annonce` WRITE;
/*!40000 ALTER TABLE `annonce` DISABLE KEYS */;
INSERT INTO `annonce` VALUES (1,'Test1','test','2020-11-01',NULL,1);
/*!40000 ALTER TABLE `annonce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cours`
--

DROP TABLE IF EXISTS `cours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cours` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(200) DEFAULT NULL,
  `titre` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `fichier` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `matiere_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `matiere_id` (`matiere_id`),
  CONSTRAINT `cours_ibfk_1` FOREIGN KEY (`matiere_id`) REFERENCES `matiere` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cours`
--

LOCK TABLES `cours` WRITE;
/*!40000 ALTER TABLE `cours` DISABLE KEYS */;
/*!40000 ALTER TABLE `cours` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departement`
--

DROP TABLE IF EXISTS `departement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label_departement` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label_departement` (`label_departement`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departement`
--

LOCK TABLES `departement` WRITE;
/*!40000 ALTER TABLE `departement` DISABLE KEYS */;
INSERT INTO `departement` VALUES (1,'UFR Informatique','Département informatique1'),(5,'UFR Droit','UFR Droit'),(6,'UFR Histoire','UFR Histoire'),(7,'UFR Math','Math');
/*!40000 ALTER TABLE `departement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `etudiant`
--

DROP TABLE IF EXISTS `etudiant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `etudiant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom_etud` varchar(60) DEFAULT NULL,
  `prenom_etud` varchar(60) DEFAULT NULL,
  `sexe_etud` varchar(60) DEFAULT NULL,
  `formation_id` int(11) DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `num_etud` varchar(60) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `adresse` varchar(60) DEFAULT NULL,
  `code_postal` int(11) DEFAULT NULL,
  `pays` varchar(60) DEFAULT NULL,
  `ville` varchar(60) DEFAULT NULL,
  `type` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_etudiant_email` (`email`),
  KEY `formation_id` (`formation_id`),
  KEY `ix_etudiant_nom_etud` (`nom_etud`),
  KEY `ix_etudiant_prenom_etud` (`prenom_etud`),
  KEY `ix_etudiant_sexe_etud` (`sexe_etud`),
  KEY `ix_etudiant_date_naissance` (`date_naissance`),
  KEY `ix_etudiant_num_etud` (`num_etud`),
  CONSTRAINT `etudiant_ibfk_1` FOREIGN KEY (`formation_id`) REFERENCES `formation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etudiant`
--

LOCK TABLES `etudiant` WRITE;
/*!40000 ALTER TABLE `etudiant` DISABLE KEYS */;
INSERT INTO `etudiant` VALUES (1,'etudiant','etudiant','M',1,'1994-04-12','etudiant@gmail.com','9999998','etudiant',NULL,NULL,NULL,NULL,'etud'),(2,'etudiant1','etudiant1','F',1,'1994-04-12','etudiant1@gmail.com','999999999','etudiant1',NULL,NULL,NULL,NULL,'etud');
/*!40000 ALTER TABLE `etudiant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formation`
--

DROP TABLE IF EXISTS `formation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `formation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label_formation` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `departement_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label_formation` (`label_formation`),
  KEY `departement_id` (`departement_id`),
  CONSTRAINT `formation_ibfk_1` FOREIGN KEY (`departement_id`) REFERENCES `departement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formation`
--

LOCK TABLES `formation` WRITE;
/*!40000 ALTER TABLE `formation` DISABLE KEYS */;
INSERT INTO `formation` VALUES (1,'Master 1 Informatique','master 1 informatique',1),(3,'Master 2 Informatique','Master 2 Informatique',1);
/*!40000 ALTER TABLE `formation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matiere`
--

DROP TABLE IF EXISTS `matiere`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `matiere` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label_matiere` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `formation_id` int(11) DEFAULT NULL,
  `professeur_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label_matiere` (`label_matiere`),
  KEY `formation_id` (`formation_id`),
  KEY `professeur_id` (`professeur_id`),
  CONSTRAINT `matiere_ibfk_1` FOREIGN KEY (`formation_id`) REFERENCES `formation` (`id`),
  CONSTRAINT `matiere_ibfk_2` FOREIGN KEY (`professeur_id`) REFERENCES `professeur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matiere`
--

LOCK TABLES `matiere` WRITE;
/*!40000 ALTER TABLE `matiere` DISABLE KEYS */;
INSERT INTO `matiere` VALUES (1,'Outils Libre','module outils libre',1,NULL),(2,'Programmation','Programmation',1,3);
/*!40000 ALTER TABLE `matiere` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professeur`
--

DROP TABLE IF EXISTS `professeur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `professeur` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom_prof` varchar(60) DEFAULT NULL,
  `prenom_prof` varchar(60) DEFAULT NULL,
  `sexe_prof` varchar(60) DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `adresse` varchar(60) DEFAULT NULL,
  `code_postal` int(11) DEFAULT NULL,
  `pays` varchar(60) DEFAULT NULL,
  `ville` varchar(60) DEFAULT NULL,
  `type` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_professeur_email` (`email`),
  KEY `ix_professeur_nom_prof` (`nom_prof`),
  KEY `ix_professeur_prenom_prof` (`prenom_prof`),
  KEY `ix_professeur_sexe_prof` (`sexe_prof`),
  KEY `ix_professeur_date_naissance` (`date_naissance`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professeur`
--

LOCK TABLES `professeur` WRITE;
/*!40000 ALTER TABLE `professeur` DISABLE KEYS */;
INSERT INTO `professeur` VALUES (3,'prodesseur','professeur','M','1981-09-06','professeur@gmail.com','professeur','9 rue prince',75000,'FRANCE','PARIS','prof'),(4,'professeur2','professeur2','M','1981-09-06','professeur2@gmail.com','professeur2','19 rue pierre',94800,'FRANCE','VILLEJUIF','prof');
/*!40000 ALTER TABLE `professeur` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-03 15:57:23
