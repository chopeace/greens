%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1> Contact List</h1>
<ul>
%for row in rows:
	<li><a href=http://cmpt470.csil.sfu.ca:8017/peace/exer8/edit/{{row[0]}}>{{row[1]}} {{row[2]}}</a>
%end
</ul>
<a href=http://cmpt470.csil.sfu.ca:8017/peace/exer8/new>new contact</a>
