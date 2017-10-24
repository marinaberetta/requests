<?php
// model
class Values
{
	public $n1;
	public $n2;
	public $soma;
}

// create instance and set a book name
$vals      =new Values();
$vals->n1=5;
$vals->n2=8;

// initialize SOAP client and call web service function
$client=new SoapClient('http://localhost/soap2/server.php?wsdl',['trace'=>1,'cache_wsdl'=>WSDL_CACHE_NONE]);

// dump response
try {
	$resp  =$client->soma($vals);
	var_dump($resp);
} catch (Exception $e) {
	var_dump($e);
    echo($client->__getLastResponse());
    echo PHP_EOL;
    echo($client->__getLastRequest());
}

?>