<?php

    /**
    * API that consumes the elements in a database
    * @author Code_Pain
    * Invoke the getEnglish method creating an instance of the RecoveryWords class, basically it recovers all the words of said language
    * existing in the database.
    */

    /**
     * Method that prompts the browser to present the retrieved information in Json format
     */
    header('Content-Type: application/json');
    
    /**
      * Since we want to create an instance of the RecoveryWords class, we include the file where it is defined
      */
    include_once 'recoveryWords.php';

    $api = new RecoveryWords();

    $api->getEnglish();
    
?>