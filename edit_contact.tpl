%#template for editing a contack
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Edit Contact</title>
<link rel="stylesheet" href="/contact/static/style.css" type="text/css" />
</head>
<body>
<h1>Edit Contact</h1>

<form action="/peace/exer8/edit/{{no}}" method="get">

<dl class="form">
<dt><label for="id_first_name">First name: <span class="required">*</span></label></dt><dd>

<div class="field"><input id="id_first_name" maxlength="100" name="first_name" type="text" value="{{old[1]}}" required/></div>
</dd>
<dt><label for="id_last_name">Last name: <span class="required">*</span></label></dt><dd>

<div class="field"><input id="id_last_name" maxlength="100" name="last_name" type="text" value="{{old[2]}}" required/></div>
</dd>
<dt><label for="id_email">Email:</label></dt><dd>

<div class="field"><input id="id_email" maxlength="75" name="email" type="email" value="{{old[3]}}" /></div>
</dd>
<dt><label for="id_phone">Phone Number:</label></dt><dd>

<div class="field"><input id="id_phone" maxlength="20" name="phone" type="text" value="{{old[4]}}" /></div>
</dd>
<dt><label for="id_notes">Notes:</label></dt><dd>

<div class="field"><textarea cols="40" id="id_notes" name="notes" rows="10">{{old[5]}}
</textarea></div>
<div class="helptext">Any additional notes on the contact info</div>
</dd>
</dl>
<p class="helptext"><span class="required">*</span> This field is required.</p>
<p><input type="submit" name="save"  value="save" /></p>
</form>


</body>
</html>




