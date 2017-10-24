<?php
// phpinfo();
// turn off WSDL caching
ini_set("soap.wsdl_cache_enabled","0");

// model, which uses in web service functions as parameter
class Values
{
	public $n1;
	public $n2;
	public $soma;
}

/**
 * Determines published year of the book by name.
 * @param Book $book book instance with name set.
 * @return int published year of the book or 0 if not found.
 */
function soma($vals)
{
	return $vals->n1+$vals->n2;
}

// initialize SOAP Server
$server = new SoapServer("test.wsdl",[
	'classmap'=>[
		'vals'=>'Values', // 'book' complex type in WSDL file mapped to the Book PHP class
	]
]);

// register available functions
$server->addFunction('soma');

// start handling requests
$server->handle();

?>