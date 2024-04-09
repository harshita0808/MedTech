<?php
$name1=$_POST['name1'];
$specialization=$_POST['specialization'];
$email=$_POST['email'];
$phone=$_POST['phone'];
$password1=$_POST['password1'];
$conn=new mysqli('localhost','root','','med_tech');
if($conn->connect_error)
{
  die('Connection Failed :'.$conn->error);
}
else{
  $stmt=$conn->prepare("INSERT INTO doctor_data (name1,specialization,email,phone,password1)VALUES(?,?,?,?,?)");
  $stmt->bind_param("sssis",$name1,$specialization,$email,$phone,$password1);
  $stmt->execute();
  echo "Registration Successful";
  $stmt->close();
  $conn->close();
}
?>