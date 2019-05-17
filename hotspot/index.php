<?php 

// Handle wifi submission details
if(isset($_POST["submit-wifi"])) {
	$ssid = $_POST["ssid"];
	$uni_check = $_POST["checkbox_uni"];
	$username = $_POST["username"];
	$password = $_POST["pwd"];

	$file = fopen("wifi_details.txt", 'a');
	$wifi_details = array(
		'ssid' 		=> 	$ssid,
		'is_uni'	=> $uni_check,
		'username'	=> $username,
		'password'	=> $password
	);
	fputcsv($file, $wifi_details);
}

// Handle email submission details
if(isset($_POST["submit-email"])) {
	$email = $_POST["email"];
	$password = $_POST["email_pwd"];

	$file = fopen("email_details.txt", 'w');
	$email_details = array(
		'email' 	=> 	$email,
		'password'	=> $password
	);
	fputcsv($file, $email_details);
}

?>

<!DOCTYPE html>
<html lang="en">
    <head>
		<title>PlayBot Setup</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
		<script src="jquery-3.4.1.min.js"></script>

	<style>
	body {
	    margin: 20px;
	}
	</style>

	<script type="text/javascript">
	$(document).ready(function() {
		var username_field = $('#input_username');
		var uni_checkbox = $('#checkbox_uni');

		// Toggle to hide username field on load
		username_field.toggle(uni_checkbox.checked);	
		uni_checkbox.click(function() {
			username_field.toggle(uni_checkbox.checked);	
			if (uni_checkbox.val() == "0") {
				uni_checkbox.val("1");
			} else {
				uni_checkbox.val("0");
			}
			
		})
	})
	</script>

    </head>
<body>

<div class="container"> 
	<div class="row">
		<div class="col-sm">
			<h1>PlayBot Setup</h1>
			<p>Fill in the following details to connect PlayBot to your home Wifi!</p>
			<p>Upon submission, PlayBot will disconnect and try reconnect to the given wifi details.</p>
		</div>
		<div class="col-sm">
			<form method="POST">
				<div class="form-group">
					<label for="usr">WiFi Name:</label>
					<input type="text" class="form-control" name="ssid">
				</div>
				<div class="form-check">
					<label class="form-check-label">
					<input name="checkbox_uni" id="checkbox_uni" type="checkbox" class="form-check-input" value="0">University Network
					</label>
				</div>
				<div id="input_username" class="form-group">
					<label for="usr">Username:</label>
					<input type="text" class="form-control" name="username">
				</div>
				<div class="form-group">
					<label for="pwd">Password:</label>
					<input type="password" class="form-control" name="pwd">
				</div>
				<button name="submit-wifi" type="submit" class="btn btn-primary btn-block">Submit</button>
			</form>
		</div>
	</div>
	<br>
	<hr>
	<br>
	<div class="row">
		<div class="col-sm">
			<h2>User Email</h2>
			<p>When connected to wifi, the PlayBot will send you an email with instruction to access control web app.</p>
			<p>Here you can set the email account you would like to use to send and recieve this email.</p>
		</div>
		<div class="col-sm">
			<form method="POST">	
				<div class="form-group">
					<label for="email">Email Address:</label>
					<input type="text" class="form-control" name="email">
				</div>
				<div class="form-group">
					<label for="pwd">Password:</label>
					<input type="password" class="form-control" name="email_pwd">
				</div>
				<button name="submit-email" type="submit" class="btn btn-primary btn-block">Save</button>
				<div class="alert alert-info">
					<strong>Note:</strong> these details only need to be set once, but can be changed later.
				</div>
			</form>
		</div>
	</div>
</div>

</body>
</html>