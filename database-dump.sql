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
USE flask_db;
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
INSERT INTO `administrateur` VALUES (1,'admin','admin','F',1,'1989-10-10','admin@gmail.com',0,'admin','9 rue pierre legrande',75013,'FRANCE','PARIS','admin'),(2,'superadmin','superadmin','F',6,'1989-10-09','superadmin@gmail.com',1,'superadmin','20 rue de lagarand',75020,'FRANCE','PARIS','admin'),(3,'raja','lamgarmel','F',6,'1999-10-10','raja@gmail.com',0,'raja','9 rue prince',93000,'FRANCE','ST DENIS','admin');
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `annonce`
--

LOCK TABLES `annonce` WRITE;
/*!40000 ALTER TABLE `annonce` DISABLE KEYS */;
INSERT INTO `annonce` VALUES (1,'Point Vendredi 25/09','Pour celles et ceux que je n\'aurais pas vu aujourd\'hui, un mail pour\r\nvous rappeler (ou vous informer) que le cours de ce soir (18h-21h) est\r\nreporté. Désolée pour ces soucis de communication cette semaine.\r\nL\'ensemble des cours aura lieu la semaine prochaine. Je reviens vers\r\nvous en début de semaine prochaine pour vous donner toutes les\r\ninformations supplémentaires.','2020-11-10',NULL,1),(4,'Cours à 15h','Votre cours de 15h est maintenu avec M. Mariage à l\'horaire et salle\r\ninitiale. Pour la suite, nous sommes en train de finaliser le point avec\r\nl\'ensemble des enseignants, vous aurez des nouvelles de ma part ou de la\r\npart de vos responsables de formation/ de vos enseignants.','2020-11-10',NULL,1),(7,'[COURS PROGRAMMATION CONCURRENTE] – Paris VIII : Visio des cours',' Bonjour à tous,\r\n\r\nCi-joint le lien de la visio pour le cours d\'aujourd\'hui et ceux à venir :\r\n\r\nhttps://meet.google.com/kvk-guxa-isq','2020-11-10',1,NULL),(8,'Absence cours','Je vous informe donc (en retard j\'en suis désolée) que le cours de M.\r\nMariage n\'aura pas lieu aujourd\'hui.\r\nIl sera reporté ultérieurement.\r\n\r\nTrès cordialement,\r\nMarie Chailloux\r\nSecrétariat Informatique.','2020-11-10',NULL,1),(11,'Cours 22/10','Bonjour à toutes et à tous,\r\n\r\nJ’espère que vous allez bien, \r\n\r\nvoici le lien meet : https://meet.google.com/vnz-cevr-tzq\r\n\r\net le support du cours.','2020-11-10',2,NULL),(15,'justificatif déplacement','Bonjour à tous,\r\nPour éviter des soucis, t même si le cours semble être avancé, je vous\r\nenvoie une attestation vous permettant de vous déplacer le mercredi,\r\nsignée par l\'UFR, dans le cadre du couvre feu.\r\nN\'hésitez pas à faire également une attestation individuelle pour\r\ncompléter si besoin.\r\nTrès cordialement,','2020-11-10',NULL,1),(16,'[COURS PROGRAMMATION CONCURRENTE – Paris VIII] : Support/Informations importantes sur l\'organisation','Bonjour à tous,\r\nMerci à chacun pour le rendu du TP1. Je vous ferai un retour plus général durant le cours prochain afin que vous puissiez prendre connaissance des remarques.\r\nCertains d\'entres vous n\'en pas bien repecté les consignes du rendu en question. Pour cela , je vous invite tous à bien lire et respecter les consignes citées dans le document ci-joint.\r\nBon courage à tous','2020-11-10',1,NULL),(17,'Update Cours 08/10','Bonjour à toutes et à tous,\r\nPour les nouveaux arrivants :\r\nVoila le lien, Mot de passe de la VM ( ubuntu ): ( taper deux fois espace ) :  https://www.transfernow.net/aIqxMR102020\r\nEn PJ une mise à jour du cours , merci de télécharger cette version.\r\nPour demain, vers 18h, je vous partagerai le lien de ZOOM.\r\nPrenez soin de vous \r\nCordialement,','2020-11-10',2,NULL),(18,'Pause pédagogique','Bonjour à tous.e.s,\r\n\r\nJuste pour vous rappeler, cette semaine du 07/11 au 11/11 est une semaine de pause pédagogique.\r\nVous n\'avez pas de cours à dispenser.\r\nPar ailleurs, pour l\'instant, j\'ai reçu une dizaine de propositions de binômes que j\'ai accepté.','2020-11-09',NULL,1),(19,'Annonce test ','raja@gmail.com','2020-11-10',NULL,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cours`
--

LOCK TABLES `cours` WRITE;
/*!40000 ALTER TABLE `cours` DISABLE KEYS */;
INSERT INTO `cours` VALUES (1,'COURS','Python','Cours de pyhon','attestation-2020-10-21_13-07.pdf','2020-11-08',2),(2,'TD','Intelligence Artificielle','TP 3 du cours de l\'Intelligence Artificielle, à rendre avant minuit','paris7.png','2020-11-08',2),(3,'NOTES','Test','for tests','attestation-2020-10-21_13-07.pdf','2020-11-08',2),(4,'COURS','Test2','2','TP1_LAMGARMEL_RAJA.txt','2020-11-08',2),(5,'TP','Python','Python IA','CMakeLists.txt','2020-11-09',1);
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
INSERT INTO `departement` VALUES (1,'UFR Informatique','UFR informatique'),(5,'UFR Droit','UFR Droit'),(6,'UFR Histoire','UFR Histoire'),(7,'UFR Math','UFR Maths');
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etudiant`
--

LOCK TABLES `etudiant` WRITE;
/*!40000 ALTER TABLE `etudiant` DISABLE KEYS */;
INSERT INTO `etudiant` VALUES (1,'LAMGARMEL','Raja','M',1,'1994-04-12','lamgarmel@gmail.com','9999998','etudiant','4 rue le provence',92000,'FRANCE','PUTEAUX','etud'),(2,'IZDI','Fatimaezzahra','F',1,'1991-01-01','izdi@gmail.com','999999999','etudiant1','9 rue pierre legrand',75000,'FRANCE','PARIS','etud'),(3,'raja','lam','M',3,'1999-10-10','raja@gmail.com','1111111','1999-10-10',NULL,NULL,NULL,NULL,'etud'),(4,'tom','tom','M',4,'1989-10-09','tom@gmail.com','999999','1989-10-09',NULL,NULL,NULL,NULL,'etud'),(6,'KERT','Aissa','M',1,'1990-01-01','kert@gmail.com','134455','1999-10-10','9 rue de lille',75000,'FRANCE','PARIS','etud'),(7,'ALLON','LEVY','M',1,'1990-01-01','allon@gmail.com','9999999','1990-01-01',NULL,NULL,NULL,NULL,'etud'),(8,'BACARD','HUGO','M',1,'1990-01-01','bacard@gmail.com','9999999','1990-01-01',NULL,NULL,NULL,NULL,'etud'),(9,'BAKER','MATTHEW','M',1,'1990-01-01','baker@gmail.com','9999999','1990-01-01',NULL,NULL,NULL,NULL,'etud'),(10,'BALWE','CHETAN','M',1,'1990-01-01','balwe@gmail.com','9999999','1990-01-01',NULL,NULL,NULL,NULL,'etud');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formation`
--

LOCK TABLES `formation` WRITE;
/*!40000 ALTER TABLE `formation` DISABLE KEYS */;
INSERT INTO `formation` VALUES (1,'Master 1 Informatique','master 1 informatique',1),(3,'Master 2 Informatique','Master 2 Informatique',1),(4,'Master 1 Histoire','UFR Histoire',6),(5,'Master 2 Histoire','Histoire',6);
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matiere`
--

LOCK TABLES `matiere` WRITE;
/*!40000 ALTER TABLE `matiere` DISABLE KEYS */;
INSERT INTO `matiere` VALUES (1,'Outils libres pour le développement logiciel','Module Outils libres pour le développement logiciel',1,9),(2,'Programmation concurrente','Module Programmation concurrente',1,11),(3,'Techniques d’apprentissage artificiel','Module Intelligence artificielle',1,7),(4,'Conférences Industrielles','Module Conférences Industrielles',1,8),(5,'Robotique et aide au diagnostic ','Module Robotique et aide au diagnostic ',1,6),(6,'Probabilités et statistiques','Probabilités et statistiques',1,10),(7,'Interfaces Homme Machine','Interfaces Homme Machine',1,12);
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professeur`
--

LOCK TABLES `professeur` WRITE;
/*!40000 ALTER TABLE `professeur` DISABLE KEYS */;
INSERT INTO `professeur` VALUES (3,'FND','Jack','M','1981-09-06','professeur@gmail.com','professeur','9 rue princee',75000,'FRANCE','PARIS','prof'),(4,'TALIBI','Youssef','M','1981-09-06','talibi@gmail.com','professeur2','19 rue pierre',94800,'FRANCE','VILLEJUIF','prof'),(5,'BUILLSON','Franck','M','1989-10-09','franck@gmail.com','1989-10-09','98 Impasse',75011,'FRANCE','PARIS','prof'),(6,'Seddiki','Lynda','F','1990-01-01','seddiki@gmail.com','1990-01-01','9 rue lyon',75000,'FRANCE','PARIS','prof'),(7,'Mariage','Jean','M','1990-01-01','mariage@gmail.com','1990-01-01','12 rue de provence',75000,'FRANCE','PARIS','prof'),(8,'Ali Chérif','Arab','M','1990-01-01','arab@gmail.com','1990-01-01','9 rue de lille',94000,'FRANCE','VILLEJUIF','prof'),(9,'Berrouachedi','Abdelghani','M','1990-01-01','berrouachedi@gmail.com','1990-01-01','9 rue pierre legrande',75000,'FRANCE','PARIS','prof'),(10,'Akdag','Herman','M','1990-01-01','akdag@gmail.com','1990-01-01','9 rue de ST etienne',92000,'FRANCE','PUTEAUX','prof'),(11,'Mehhadi','Ilyes','M','1990-01-01','mehhadi@gmail.com','1990-01-01','9 rue de lyon',75000,'FRANCE','PARIS','prof'),(12,'Ammi','Mehdi','M','1990-01-01','ammi@gmail.com','1990-01-01','9 rue pierre legrand',75000,'FRANCE','PARIS','prof');
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

-- Dump completed on 2020-11-10 15:06:11
