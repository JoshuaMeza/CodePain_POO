<?php
   /**
   * API that consumes the elements in a database
   * @author Code_Pain
   * Create the RecoveryWords class, which is in charge of defining the methods that will be called by the different functionalities
   * from the API
   */
  /**
   *   Since we want to create an instance of the Words class, we include the file where it is defined
   */ 
include_once 'words.php';

class RecoveryWords{

    /**
    * Declaration of the only variable to use
    * @param word: basically create an instance of Words to be able to invoke its information retrieval methods
    */
    private $word;

     /**
     * Variable word constructor method, basically defines the aforementioned
     */

    public function __construct(){
        $this->word = new Words();
    }


    /**
      * Method that is in charge of recovering all the words of all the languages of the database storing them in an array,
      * later encode it in Json format, in case the database is empty it prints the same
      * @return words: array with retrieved words
      */

    function getAll(){
        $words = array();
        $words["English"] = array();
        $words["Spanish"] = array();
        $words["Mayan"] = array();

        $res = $this->word->getAllWords();

        if($res->rowCount()){
            while ($row = $res->fetch(PDO::FETCH_ASSOC)){
                if($row['languageID']=='1'){
                    array_push($words["English"], $row['word']);
                } else {
                    if ($row['languageID']=='2'){
                        array_push($words["Spanish"], $row['word']);
                    } else {
                        array_push($words["Mayan"], $row['word']);
                    }
                }
                
            }
        
            echo json_encode($words);
        }else{
            echo json_encode(array('mensaje' => 'No hay elementos'));
        }
    }

   /**
      * Method that is responsible for retrieving all the words in Spanish from the database by storing them in an array,
      * later encode it in Json format, in case the database is empty it prints the same
      * @return words: array with retrieved words
      */
    function getSpanish(){
        $words = array();

        $res = $this->word->getSpanishWords();

        if($res->rowCount()){
            while ($row = $res->fetch(PDO::FETCH_BOTH)){

                array_push($words, $row['word']);
            }
        
            echo json_encode($words);
        }else{
            echo json_encode(array('mensaje' => 'No hay elementos'));
        }
    }
      /**
      * Method that is responsible for retrieving all the words in English from the database by storing them in an array,
      * later encode it in Json format, in case the database is empty it prints the same
      * @return words: array with retrieved words
      */
    function getEnglish(){
        $words = array();

        $res = $this->word->getEnglishWords();

        if($res->rowCount()){
            while ($row = $res->fetch(PDO::FETCH_BOTH)){

                array_push($words, $row['word']);
            }
        
            echo json_encode($words);
        }else{
            echo json_encode(array('mensaje' => 'No hay elementos'));
        }
    }
     /**
      * Method that is responsible for retrieving all the words in Mayan from the database by storing them in an array,
      * later encode it in Json format, in case the database is empty it prints the same
      * @return words: array with retrieved words
      */
    function getMayan(){
        $words = array();

        $res = $this->word->getMayanWords();

        if($res->rowCount()){
            while ($row = $res->fetch(PDO::FETCH_BOTH)){

                array_push($words, $row['word']);
            }
        
            echo json_encode($words);
        }else{
            echo json_encode(array('mensaje' => 'No hay elementos'));
        }
    }
}

?>