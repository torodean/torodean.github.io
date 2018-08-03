<?php
$field_name = $_POST['cf_name'];
$field_email = $_POST['cf_email'];
$field_message = $_POST['cf_message'];
$field_reason = $_POST['cf_reason'];
$field_found = $_POST['cf_found'];

$mail_to = 'awtorode@gmail.com';
$subject = 'Message from '.$field_name.' regarding '.$field_reason;

$body_message = 'From: '.$field_name."\n";
$body_message .= 'E-mail: '.$field_email."\n";
$body_message .= 'Reason: '.$field_reason."\n";
$body_message .= 'Found us: '.$field_found."\n";
$body_message .= 'Message: '.$field_message;

$headers = 'From: '.$field_email."\r\n";
$headers .= 'Reply-To: '.$field_email."\r\n";

$mail_status = mail($mail_to, $subject, $body_message, $headers);

if ($mail_status) { ?>
	<script language="javascript" type="text/javascript">
		alert('Thank you for the message. We will contact you shortly.');
		window.location = 'index.html#contact';
	</script>
<?php
}
else { ?>
	<script language="javascript" type="text/javascript">
		alert('Message failed. Please, send an email to awtorode@gmail.com');
		window.location = 'index.html#contact';
	</script>
<?php
}
?>