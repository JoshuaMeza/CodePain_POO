<?php
/**
   * API that consumes the elements in a database
   * @author Code_Pain
   * Create Words extends Connect class, which is responsible for creating 
   * the methods to retrieve specific information from the database
   */

  /**
   *   As we want to create an extension of the Connect class, we include the file where it is defined
   */ 
include_once 'connect.php';

class Words extends Connect{
    
    /**
      * Method that retrieves all the words regardless of the language, within the database
      * @return query: stores the aforementioned to be manipulated
      */
    function getAllWords(){
        $query = $this->connect()->query('SELECT * FROM Words ORDER BY `word`  ASC');
        return $query;
    }

    /**
        * Method that retrieves all the words in English, within the database
        * @return query: stores the aforementioned to be manipulated
        */
    function getEnglishWords(){
        $query = $this->connect()->query('SELECT word FROM Words WHERE languageID = "1" ORDER BY `word`  ASC');
        return $query;
    }
        /**
        * Method that retrieves all the words in Spanish, within the database
        * @return query: stores the aforementioned to be manipulated
        */
    function getSpanishWords(){
        $query = $this->connect()->query('SELECT word FROM Words WHERE languageID = "2" ORDER BY `word`  ASC ');
        return $query;
    }
        /**
        * Method that retrieves all the words in Mayan, within the database
        * @return query: stores the aforementioned to be manipulated
        */
    function getMayanWords(){
        $query = $this->connect()->query('SELECT word FROM Words WHERE languageID = "3" ORDER BY `word`  ASC');
        return $query;
    }
}

?>