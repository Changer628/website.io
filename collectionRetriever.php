$url = "http://maps.google.com/maps/api/directions/xml?origin=Quentin+Road+Brooklyn%2C+New+York%2C+11234+United+States&destination=550+Madison+Avenue+New+York%2C+New+York%2C+10001+United+States&sensor=false";
$xml = simplexml_load_file($url);
print_r($xml);