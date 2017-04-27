<?php
 
 if($_SERVER['REQUEST_METHOD']=='POST'){
 
 $image = $_POST['image'];
                $name = $_POST['name'];
 
 require_once('dbConnect.php');
 
 $sql ="SELECT id FROM lateximage ORDER BY id ASC";
 
 $res = mysqli_query($con,$sql);
 
 $id = 0;
 $filename = "uploads/email.txt"; 
 while($row = mysqli_fetch_array($res)){
 $id = $row['id'];
 }
 $path = "uploads/test.png";
 
 $actualpath = "192.168.43.171/$path";

 file_put_contents( $filename, $name);
 
 $sql = "INSERT INTO lateximage (photo,name) VALUES ('$actualpath','$name')";
 
 if(mysqli_query($con,$sql)){
 file_put_contents($path,base64_decode($image));
 echo "Successfully Uploaded";
 }
 mysqli_close($con);
 }else{
 echo "Error";
 }
?>