/*--------------
  Active Links
--------------*/

function activate()
{

	
	var pathname = window.location.pathname;
	var linkbar = "";
	var footerbar = "";
	var search = "";
	
	var links = new Array();
	links[0] = "/search/";
	links[1] = "/forums/";
	links[2] = "/events/";
	links[3] = "/calendar/";
	links[4] = "/clubs/";
	links[5] = "/homepage/";
	
	var linknames = new Array();
	linknames[0] = "Search";
	linknames[1] = "Forums";
	linknames[2] = "Events";
	linknames[3] = "Calendar";
	linknames[4] = "Clubs";
	linknames[5] = "Home";
	
	for(i=0;i<=5;i++)
	{
		if(i==0)
		{
			search = " onMouseOver='searchOver();'";
		}
		else
		{
			search = "";
		}
	
		if(pathname.indexOf(links[i]) != -1)
		{
			linkbar += '<a href="'+links[i]+'"><div id = "link-10" class="active">'+linknames[i]+'</div></a>';
		}
		
		else
		{
			linkbar += '<a href="'+links[i]+'"'+search+'><div id = "link-10">'+linknames[i]+'</div></a>';
		}
		
		footerbar += '<a href="'+links[5-i]+'">'+linknames[5-i]+'</a>';
		if(i!=5) footerbar += ' | ';
	}		
	
	footerbar += "<br><center><div id='poweredby-32' ";
	footerbar += "onClick='location.href=\"https://www.djangoproject.com/\"' onmouseover=\"this.style.cursor='pointer';\"";
	footerbar += "><div id='footertext-31'>Powered by </div><div id='django-30'></div></div></center>";
	
	document.getElementById("links-bar-17").innerHTML = linkbar;
	document.getElementById("footer-14").innerHTML = footerbar;

}


/*----------------------
  Show/Hide Login Area
----------------------*/

function hidelogin()
{
	var object = document.getElementById('loginarea');
	var height = parseInt(object.offsetHeight);
	
	if(height<180)
	{
		$('#loginarea').hide();
	}
}

function showlogin()
{
	var x = 500;
	$('#loginarea').slideToggle(x);
	setTimeout('window.id_username.focus();',x);
}

/*---------------------------
  Forum Delete Confirmation
---------------------------*/

function forumDeleteConfirmation()
{
	$(".confirmation").hide();
}

function forumDelete(x)
{
	var innerDiv = "#inner"+x;
	$(innerDiv).toggle();
}

/*---------------------------
  Event Delete Confirmation
---------------------------*/

function eventDeleteConfirmation()
{
	$(".confirmation").hide();
}

function eventDelete(x)
{
	var innerDiv = "#inner"+x;
	$(innerDiv).toggle();
}

/*------------
  DatePicker
------------*/

function pickDate()
{	
	$( "#id_date" ).datepicker({ dateFormat: 'yy-mm-dd', minDate: 0 });
}

/*----------
  Calendar
----------*/

function showCalendar()
{
	$( "#calendar-38" ).datepicker({ dateFormat: 'yy/mm/dd' });
	updateDateButton();
}

function gotoDate()
{
	var calendarDate = document.getElementById("calendar-38").value;
	location.href = "/events/"+calendarDate+"/";
}

function updateDateButton()
{
	var content;
	var calendarDate = document.getElementById("calendar-38").value;
	document.getElementById("dateButton").innerHTML="View Events for "+calendarDate;
}

/*---------
  Remodel
---------*/

function remodel()
{
	var top = document.getElementById("welcome-header-36");
	var center = document.getElementById("login-15");
	var bottom = document.getElementById("footer-26");

	var topHeight = parseInt(top.offsetHeight);
	var centerHeight = parseInt(center.offsetHeight);
	
	var winW = 630, winH = 460;
	if (document.body && document.body.offsetWidth) {
	 winW = document.body.offsetWidth;
	 winH = document.body.offsetHeight;
	}
	if (document.compatMode=='CSS1Compat' &&
		document.documentElement &&
		document.documentElement.offsetWidth ) {
		 winW = document.documentElement.offsetWidth;
		 winH = document.documentElement.offsetHeight;
	}
	if (window.innerWidth && window.innerHeight) {
		 winW = parseInt(window.innerWidth);
		 winH = parseInt(window.innerHeight);
	}
	
	var bottomHeight = winH-topHeight-centerHeight-20;
	bottom.style.height = bottomHeight+"px";
}

/*-----------
  Event Map
-----------*/

function hideMapArea()
{
	$("#mapArea").slideUp();
}

function eventMap(venue)
{
	var thisVenue="http://maps.ntu.edu.sg/maps#q:"+venue;
	var mapAreaString="<iframe src='";
	mapAreaString += thisVenue;
	mapAreaString += "' width = 100% height = 500><p>Your browser does not support iframes.</p></iframe>";
	mapAreaString += "<p onclick='hideMapArea();'><a href = '#'>Click here to hide this map</a></p>";
	document.getElementById("mapArea").innerHTML=mapAreaString;
	$("#mapArea").slideDown();
}

/*--------
  Search
--------*/

function hideSearchBox()
{
	$("#searchBox-33").hide();
}

function searchOver()
{
	$("#searchBox-33").slideDown();
}

function rehideSearchBox()
{
	$("#searchBox-33").slideUp();
}

/*---------------
  Add Event Map
---------------*/

function clickVenueId()
{
	document.getElementById("id_venue").onblur= function()
	{
		var venue=id_venue.value;
		var thisVenue="http://maps.ntu.edu.sg/maps#q:"+venue;
		var mapAreaString="<iframe src='";
		mapAreaString += thisVenue;
		mapAreaString += "' width = 100% height = 400><p>Your browser does not support iframes.</p></iframe>";
		document.getElementById("mapAreaII").innerHTML=mapAreaString;
		id_venue.value = id_venue.value.toUpperCase();
	}
}

function hideVenueId()
{
	$('#mapAreaII').slideUp();
}



//--------OBSOLETE--------

/*---------------
  Calendar Test
---------------*/

function testCalendar()
{
	var place = document.getElementById("calendar-event-16");
	$("#calendar-event-16").hide();
	
	$('#event20').click(function() {
		place.innerHTML = "<h3>Events on the 20th</h3><p><a href = 'anevent.html'>In vel turpis sed enim facilisis lacinia sit amet elit.</a></p>";
		$("#calendar-event-16").slideDown("slow");
		//remodel();
	});
}

/*-----------
  Messaging
-----------*/

function messaging()
{
	var place = document.getElementById("main-6");
	var inbox = "<h3>My Messages</h3><hr>";
	inbox += '<table width = 100% border=1 class = messages>';
	inbox += '<tr><th>From<th>Subject';
	inbox += '<tr class = "contentpane"><td colspan = 2>';
	inbox += '<tr><td>X<td><a href = "#"><div onclick = "openMessage(\'1\');">Mauris consectetur, sapien non commodo.</div></a>';
	inbox += '<tr class = "contentpane"><td colspan = 2><div id = "message1"></div>';
	inbox += '<tr><td>Y<td><a href = "#"><div onclick = "openMessage(\'2\');">Pellentesque ut gravida lectus. Donec.</div></a>';
	inbox += '<tr class = "contentpane"><td colspan = 2><div id = "message2"></div>';
	inbox += '<tr><td>Z<td><a href = "#"><div onclick = "openMessage(\'3\');">Donec at leo nec lorem cursus aliquet ac in urna.</div></a>';
	inbox += '<tr class = "contentpane"><td colspan = 2><div id = "message3"></div>';
	inbox += '<tr><td>A<td><a href = "#"><div onclick = "openMessage(\'4\');">Donec nec magna vitae leo hendrerit semper.</div></a>';
	inbox += '<tr class = "contentpane"><td colspan = 2><div id = "message4"></div>'
	
	place.innerHTML = inbox;
	
	$("#message1").hide();
	$("#message2").hide();
	$("#message3").hide();
	$("#message4").hide();
	
	//remodel();
}

function openMessage(message)
{
	var place = document.getElementById("message"+message);
	//$("#message"+message).hide();
	place.style.padding = "12px";
	place.innerHTML = "In congue ullamcorper elit. Sed accumsan ipsum a massa placerat vehicula. Nunc malesuada gravida sem nec porttitor. Sed laoreet nisi vitae elit consectetur pretium. Quisque id mi leo, et ullamcorper leo. Nulla laoreet, massa eu tristique accumsan, risus nisl sagittis lorem, in pellentesque mauris neque non ipsum. Nullam id odio odio, ac adipiscing felis. Donec dictum, lectus ut facilisis dictum, purus ante aliquet eros, sed pretium sem metus ac est. Duis vitae commodo orci. Duis in facilisis magna. Vivamus justo quam, feugiat non accumsan at, interdum eu sapien. Maecenas eget ullamcorper lorem.";
	$("#message"+message).slideToggle(490);
	//setTimeout('remodel();',500);
}

/*--------
  Forums
--------*/

var topicNo = 0;
var postNo = 0;

var thread = new Array();
var poster = new Array();

for(i=0;i<=2;i++)
{
	thread[i] = new Array();
	poster[i] = new Array();
}

thread[0][0] = "Donec in nibh id massa gravida rutrum.";
thread[0][1] = "Sed lectus massa, pretium nec blandit eu, cursus et velit. Nulla facilisi. Proin ut nisl enim. Etiam suscipit, orci quis fermentum commodo, massa eros cursus risus, vitae commodo risus purus et risus.";
thread[0][2] = "Etiam laoreet dignissim iaculis. Donec lacinia, massa vitae ultrices interdum, mi felis eleifend massa, at accumsan felis nibh a urna.";
thread[0][3] = "Cras auctor odio sit amet neque vehicula ultrices. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut tempus consectetur lacus, a venenatis nibh dignissim id. Ut nibh leo, iaculis sed pretium eu, auctor sed nisi.";
poster[0][1] = "<img src = 'images/avatar.jpg'><p>X</p>";
poster[0][2] = "<img src = 'images/avatar2.jpg'><p>Y</p>";
poster[0][3] = "<img src = 'images/avatar3.jpg'><p>Z</p>";

thread[1][0] = "Pellentesque ut ipsum metus, id bibendum mi.";
thread[1][1] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ultricies neque ut est molestie auctor. Cras velit dui, placerat vitae vestibulum non, varius vel nisi.";
thread[1][2] = "Donec quis eros dolor, non suscipit elit. Nullam pellentesque ullamcorper libero, non imperdiet velit porttitor vel.";
thread[1][3] = "Integer vitae lorem ut lacus pharetra rutrum. Proin vestibulum magna eget dolor molestie ac sollicitudin magna ultricies.";
thread[1][4] = "Duis faucibus, dui quis tristique laoreet, justo lectus lobortis elit, sit amet scelerisque lacus lectus a metus.";
thread[1][5] = "Vestibulum dictum arcu in lacus mollis porta. Morbi id eros magna. Praesent imperdiet dui sit amet nisl lobortis et hendrerit turpis pharetra.";
poster[1][1] = "<img src = 'images/avatar.jpg'><p>X</p>";
poster[1][2] = "<img src = 'images/avatar2.jpg'><p>Y</p>";
poster[1][3] = "<img src = 'images/avatar3.jpg'><p>Z</p>";
poster[1][4] = "<img src = 'images/avatar.jpg'><p>X</p>";
poster[1][5] = "<img src = 'images/avatar2.jpg'><p>Y</p>";

thread[2][0] = "Morbi auctor dolor nibh, congue aliquam purus.";
thread[2][1] = "Sed varius, magna sed vulputate bibendum, lacus sapien tincidunt odio, et lobortis velit libero porta dolor.";
thread[2][2] = "Nunc sit amet sapien vel mi vehicula fringilla. Phasellus diam ante, pharetra eget suscipit at, interdum sit amet felis.";
thread[2][3] = "Pellentesque lectus lectus, hendrerit quis consequat vel, vehicula in turpis.";
thread[2][4] = "Maecenas quis scelerisque nisl. Etiam interdum consequat augue ut convallis.";
poster[2][1] = "<img src = 'images/avatar.jpg'><p>X</p>";
poster[2][2] = "<img src = 'images/avatar2.jpg'><p>Y</p>";
poster[2][3] = "<img src = 'images/avatar3.jpg'><p>Z</p>";
poster[2][4] = "<img src = 'images/avatar.jpg'><p>X</p>";

function forums()
{
	var place = document.getElementById("main-6");
	var forums = "<h3>My Forums</h3><hr>";
	forums += '<table width = 100% border=1 class = forums>';
	forums += '<tr><th>Forum<th>Topics';
	forums += '<tr><td align = center>3<td><a href = "#"><div onclick = "openForumAnim1();">NTU Students Union</div></a>';
	
	place.innerHTML = forums;
}

function openForumAnim1()
{
	$("#main-6").slideToggle("500");
	setTimeout('openForum2();',510);
}

function openForum2()
{
	var forums = "<h3>Students Union Forums</h3><hr>";
	forums += '<table width = 100% class = forums>';
	forums += '<tr><th width = 10%>Posts<th width = 90%>Topic';
	for(i=0;i<=2;i++) forums += '<tr><td align = "center" valign = "middle">'+(thread[i].length-1)+'<td><a href="#"><div onclick = "topicNo = '+i+'; openForumAnim2();"><h3>'+thread[i][0]+'</h3><br><i>'+thread[i][1].slice(0,200)+'...</i></div></a>';
	
	document.getElementById("main-6").innerHTML = forums;
	$("#main-6").slideToggle("500");
}

function openForumAnim2()
{
	$("#main-6").slideToggle("500");
	setTimeout('openForum3();',510);
}

function openForum3()
{
	var forums = '<a href ="#"><div onclick = "openForumAnim1();"><<</div></a>';
	forums += '<h3>'+thread[topicNo][0]+'</h3><hr>';
	forums += '<table width = 100% class = forums>';
	for(i=1;i<thread[topicNo].length;i++) forums += '<tr><td width = 20% align = center>'+poster[topicNo][i]+'<td width = 80% onmouseover = "postNo = '+i+'; showTextbox();"><div id = "postarea"><table width = 100% height = 100%><tr><td style="border: none;">'+thread[topicNo][i]+'<tr><td style="border: none;"><div id = "textbox'+i+'"><textarea class = "maxwidth" id = "textarea'+i+'" onfocus = "postNo = '+i+'; expandBox();" onblur = "postNo = '+i+'; contractBox();"></textarea></div></table></div>';
	
	document.getElementById("main-6").innerHTML = forums;
	
	
	
	hideTextbox()
	//showTextbox();
	
	$("#main-6").slideToggle("500");
}

function showTextbox()
{
	var divName = "#textbox"+postNo;
	$("#postarea").live("mouseenter",
		function()
		{
			$(divName , $(this)).show();
		});
	$("#postarea").live("mouseleave",
		function()
		{
			$(divName , $(this)).hide();
		}
	);
}

function hideTextbox()
{
	for(i=1;i<thread[topicNo].length;i++)
	{
		divName = "#textbox"+i;
		$(divName).hide();
	}
}

function expandBox()
{
	var divname = "#textarea"+postNo;
	$(divname).animate({height:100},"slow");
}

function contractBox()
{
	var divname = "#textarea"+postNo;
	$(divname).animate({height:50},"slow");
}