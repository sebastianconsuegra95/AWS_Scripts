<?php
$r = new HttpRequest('https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key=AIzaSyCBOaRqI8IcgcQlXj5Evtv-0KgcHccWbeM', HttpRequest::METH_GET);
$r->setOptions(array('lastmodified' => filemtime('local.rss')));
$r->addQueryData(array('category' => 3));
try {
    $r->send();
    if ($r->getResponseCode() == 200) {
        file_put_contents('local.rss', $r->getResponseBody());
    }
} catch (HttpException $ex) {
    echo $ex;
}
?>