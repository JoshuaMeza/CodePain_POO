<?php
   /**
   * API that consumes the elements in a database
   * @author Code_Pain
   * Connect class: Creates the connection with the database, in case of not being able to do so, the reason is printed
   */

class Connect{
    /**
      * The variables to use are declared, which represent information necessary to create the connection with the database
      * @param host: host where the database is stored
      * @param db: name of the database to which we want to connect
      * @param charset: type of language in which the database is encoded
      */
    private $host;
    private $db;
    private $charset;

    /**
      * Constructor method, basically assigns to the variables the aforementioned values
      */
    public function __construct(){
        $this->host     = 'localhost';
        $this->db       = 'ClasePOO';
        $this->charset  = 'utf8mb4';
    }


    /**
      * Method that tries to connect to the database taking into account the handling of the exception, that is, when it does not succeed and
      * then print the reason
      * @return pdo: the connection with the database
      */
    function connect(){
    
        try{
            $config = parse_ini_file('../../private/config.ini'); 
            $connection = "mysql:host=".$this->host.";dbname=" . $this->db . ";charset=" . $this->charset;
            $pdo = new PDO($connection,$config['user'],$config['password']);
        
            return $pdo;


        }catch(PDOException $e){
            print_r('Error connection: ' . $e->getMessage());
        }   
    }
    
}


?>