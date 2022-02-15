var showId = false;
var showClass = false;
var showIdClass = false;


// tags list;
var headingTags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'];
var headingTags0 = [], headingTags1 = [], headingTags2 = [], headingTags3 = [], headingTags4 = [], headingTags5 = [];

var html5Tags = ['header', 'nav', 'main', 'section', 'footer'];
var html5Tags0 = [], html5Tags1 = [], html5Tags2 = [], html5Tags3 = [], html5Tags4 = [];

var generalTags = ['div', 'span'];
var generalTags0 = [], generalTags1 = [];

var textTags = ['p', 'br', 'strong', 'b', 'em', 'i'];
var textTags0 = [], textTags1 = [], textTags2 = [], textTags3 = [], textTags4 = [], textTags5 = [];

var listTags = ['ul', 'ol', 'li'];
var listTags0 = [], listTags1 = [], listTags2 = [];

var anchorTags = ['a'];

var imageTags = ['img', 'picture'];
var imageTags0 = [], imageTags1 = [];

var iframeTags = ['iframe'];

// tags color:
var html5Color = ['#6600CC', '#3333CC', '#3366CC', '#3399CC', '#33CCCC', '#33FFCC'];
var generalColor = ['#FF00FF', '#FF9999'];
var headingColor = ['#f00', '#FF3300', '#FF6600', '#FF9900', '#FFCC00', '#FFFF00'];
var textColor = ['#4F004D', '#790076', '#A600A2', '#9B00D7', '#B900FF', '#CB42FF'];
var listColor = ['#73ab00', '#c3ff00', '#cbe00d'];
var anchorColor = ['#45ceff'];
var imageColor = ['#009900', '#33FF00'];
var iframeColor = ['#DE7C2C'];

function hvvDisplay(tagType, colorType) {

	// console.log(tagType);
	
	var tagTypeArray = window[tagType];

	colorType = typeof colorType === 'object' ? colorType : [colorType];

	// console.log(tagTypeArray);

	var hvvClassType = 'hvv-tagInfo' + tagType;

	for (var i = 0; i < tagTypeArray.length; i++) {
		// console.log('for')

		// If its an image, shadow style value is default, and applied outside element. If other tags, value equal 'inset':
		var shadowInner = tagTypeArray[i] == 'img' || tagTypeArray[i] == 'picture' ? ' ' : ' inset ';

		// Create style rule to ouline specific tag:
		hvvInsertStyle(tagType, tagTypeArray[i] + '{box-shadow: 0 0 0 1px ' + colorType[i] + shadowInner + '!important;}')

		// Random giant bizarre value to add to Z-index, prevent incompatibility with existent page style:
		var randomZIndex = Math.floor(Math.random() * 100000000);

		// For text tags, include 'display: inline-block' style, so the label is placed next to element:
		if (tagTypeArray[i] == 'strong' || tagTypeArray[i] == 'b' || tagTypeArray[i] == 'em' || tagTypeArray[i] == 'i' || tagTypeArray[i] == 'a') {
			hvvInsertStyle(tagType, tagTypeArray[i] + '{display: inline-block !important;}');
		}

		// console.log('tagTypeArray[i]: ' + tagTypeArray[i])

		// For every tag element:
		$(tagTypeArray[i]).each(function (index) {
			// console.log('each')

			// If its a 'div' prevent outline 'hvv-noOutline' divs created by this extension:
			if (!$(this).hasClass('hvv-noOutline')) {

				// ID attribute:

				// Get id attribute value:
				var myId = $(this).attr('id');
				var myIdFade = 'false';

				// Check if id attribute exist:
				if (myId == undefined) {
					myId = 'not found';
					myIdFade = 'true';
				}

				// Check if id attribute has no value:
				if (myId == ' ') {
					myId = 'empty value';
				}

				// Create div id display:
				var attrId = '<div class="hvv-noOutline hvv-hideId hvv-idClass" data-fade="' + myIdFade + '" > |  id: ' + myId + '</div>';


				// Class attribute:

				// Get class attribute value:
				var myCalss = $(this).attr('class');
				var myClassFade = 'false';

				// Check if class attribute exist:
				if (myCalss == undefined) {
					myCalss = 'not found';
					myClassFade = 'true';
				}

				// Check if class attribute has no value:
				if (myCalss == ' ') {
					myCalss = 'empty value';
				}

				// Create div class display:
				var attrClass = '<div class="hvv-noOutline hvv-hideClass hvv-idClass" data-fade="' + myClassFade + '" > | class: ' + myCalss + '</div>';


				// Set options with id and class:
				options = attrId + attrClass;


				// Specific tag classes:
				var hvvClasses = 'hvv-tagInfo' + tagTypeArray[i] + ' ' + hvvClassType;

				// If its an 'img' tag, get attributes:
				if (tagTypeArray[i] == 'img') {
					// Get alt attribute label
					var altText = $(this).attr('alt');

					// Configure optional label text for images:
					options += ' | alt: ' + altText;

					// Insert label after 'img' tag:
					$(this).after(hvvLabel(hvvClasses, tagTypeArray[i], options));

					// If its an 'a' tag:
				} else if (tagTypeArray[i] == 'a') {
					// Get 'target' attribute value:
					var targetText = $(this).attr('target') ? $(this).attr('target') : 'missing';
					// Get 'href' attribute value:s
					var href = $(this).attr('href');

					// Configure optional label text for anchors:
					options += ' | type: ' + hvvCheckLinkDomain(href) + ' | target: ' + targetText;

					// Append label inside 'a' tag:
					$(this).append(hvvLabel(hvvClasses, tagTypeArray[i], options));
				} else {
					// Append label inside other tags:
					$(this).append(hvvLabel(hvvClasses, tagTypeArray[i], options));
				}
			}
		});
		// Append specific tag label styles:
		hvvInsertStyle(tagType, '.hvv-tagInfo' + tagTypeArray[i] + "{" + 'background-color:' + colorType[i] + '; z-index:' + (100000000 + randomZIndex) + ';}');
	}

	// Check if there is no generic label styles block..
	if ($('#hvv-general').length == 0) {
		// ...append gerenric label styles:
		hvvInsertStyle('hvv-general', '.hvv-tagInfo{position: absolute; padding: 5px; font-size:12px; line-height:1em; font-weight:normal; text-transform: none; font-family: sans-serif; white-space: nowrap; color:#fff; text-indent: 0; border:1px solid #fff;}.hvv-tagInfo:hover, .hvv-tagInfo-hover {font-size: 18px; z-index: 10000000000000000 !important; border: 2px solid #fff; padding: 10px;} .hvv-idClass{display: inline-block; vertical-align:top; opacity: 1;} .hvv-hideId{display:none; } .hvv-showId{display:inline-block; margin-left: 5px;} .hvv-hideClass{display:none} .hvv-showClass{display:inline-block; margin-left: 5px;} .fade{ transition: 6s; opacity: 0;} .hvv-noOutline {box-shadow: none !important;}');
	}

	hvvShowId();
	hvvShowClass();
}

// Insert label
function hvvLabel(hvvClasses, tagType, options) {
	// Label + specific tag classes + tag name + tag options:
	return '<div class="hvv-tagInfo hvv-noOutline ' + hvvClasses + '" >' + tagType + options + '</div>'
}

// Create style block or append rules to an existent style block:
function hvvInsertStyle(id, rule) {
	// Get id of specific style tag block:
	var $styleTag = $('#' + id);

	// If style block already exist...
	if ($styleTag.length > 0) {
		// ... add new rule:
		$styleTag.append(rule);
	} else {
		// If its a new block, append block with specific tag id:
		$('body').append('<style id="' + id + '"></style>');
		// And append rule:
		$('#' + id).append(rule);
	}
}

// Check if anchor value is [internal, external, javascript], if its [relative, absolute], and if attribute 'target' has a value:
function hvvCheckLinkDomain(link) {
	// Get domain name:
	var thisHostName = window.location.hostname;

	// console.log(link)

	// If attribute 'href' has a value specified:
	if (link !== undefined && link !== '') {

		// Split value into an array:
		link = link.split('/');

		// Check if the first index iss 'http' or 'https':
		if (link[0] == "http" || link[0] == "https") {
			// Check if the second index is equal to this hostname:
			if (link[2] == thisHostName) {
				// href value is an absolute internal link:
				return 'internal link, absolute';
			} else {
				// href its an external link (allways absolute):
				return 'external link';
			}
			// If href value is equal to '#'...
		} else if (link[0] == '#') {
			// ...then its internal link or javascript call:
			return 'internal link or javascript call';
			// If href has 'javascript' on it...
		} else if (link[0].indexOf('javascript') > 0) {
			// ...its a javascript call:
			return 'javascript call';
			// If doesn't have 'http' or 'https'...
		} else {
			// ... href value its a relative internal link:
			return 'internal link, relative';
		}
	} else {
		// Else, herf its empty:
		return 'empty';
	}
}

function hvvShowId() {
	if (showId) {
		$('.hvv-hideId').addClass('hvv-showId');
		$('.hvv-showId').removeClass('hvv-hideId');

		var $hvvShowId = $('.hvv-showId');

		$hvvShowId.each(function (index) {
			var self = $(this);
			setTimeout(function () {
				if (self.data('fade') == true) {
					self
						.animate({ opacity: 0 }, 1000)
						.animate({ width: 0, marginLeft: 0 }, 100);
				}
			}, 2000)
		});
	} else {
		$('.hvv-showId').addClass('hvv-hideId');
		$('.hvv-hideId').removeClass('hvv-showId');
	}
}

function hvvShowClass() {
	if (showClass) {
		$('.hvv-hideClass').addClass('hvv-showClass');
		$('.hvv-showClass').removeClass('hvv-hideClass');

		var $hvvShowClass = $('.hvv-showClass');

		$hvvShowClass.each(function (index) {
			var self = $(this);
			setTimeout(function () {
				if (self.data('fade') == true) {
					self
						.animate({ opacity: 0 }, 1000)
						.animate({ width: 0, marginLeft: 0 }, 100);
				}
			}, 2000)
		});
	} else {
		$('.hvv-showClass').addClass('hvv-hideClass');
		$('.hvv-hideClass').removeClass('hvv-showClass');
	}
}

// On load extension actions:
function hvvLoadActions() {
	var hvvLoadObjs = [];

	// console.log('hvvLoadObjs: ' + hvvLoadObjs)

	// -------------------
	// 1) Add Title and Description to response object
	// ------------------

	// Get the 'title' tag:
	var $titleTag = $('title');

	// Check if there is a Title tag...:
	if ($titleTag.length > 0) {
		if ($titleTag.length < 2) {
			if ($titleTag.text() !== "") {
				// ...get its value:
				hvvLoadObjs.push($titleTag.text());
			} else {
				hvvLoadObjs.push('The title tag is empty.');
			}
		} else {
			hvvLoadObjs.push('More than 1 tilte tag found.');
		}
	} else {
		hvvLoadObjs.push('No titlte tag found.');
	}

	// Get the 'meta description' tag:
	var $descriptionTag = $('meta[name=description]');

	// console.log($descriptionTag[0]);

	// Check if there is a 'Meta Description' tag...:
	if ($descriptionTag.length > 0) {
		if ($descriptionTag.length < 2) {
			if ($descriptionTag[0].content !== "") {
				// ... get its value:
				hvvLoadObjs.push($descriptionTag[0].content);
			} else {
				hvvLoadObjs.push('The description tag is empty.');
			}
		} else {
			hvvLoadObjs.push('More than 1 description tag found.');
		}
	} else {
		hvvLoadObjs.push('No description tag found.');
	}

	// -------------------
	// 2) Add array of tag names to reponse object:
	// ------------------

	// Traverse DOM:
	hvvLoadObjs.push(hvvDomTree(document.body, 0));

	// -------------------
	// 3) Add list of all popup.html seted tag buttons to reponse object:
	// ------------------

	// List of possible Style tags IDs inserted on the page:
	var hvvStyleTags = ['headingTags', 'headingTags0', 'headingTags1', 'headingTags2', 'headingTags3', 'headingTags4', 'headingTags5', 'html5Tags', 'html5Tags0', 'html5Tags1', 'html5Tags2', 'html5Tags3', 'html5Tags4', 'generalTags', 'generalTags0', 'generalTags1', 'textTags', 'textTags0', 'textTags1', 'textTags2', 'textTags3', 'textTags4', 'textTags5', 'listTags', 'listTags0', 'listTags1', 'listTags2', 'anchorTags', 'imageTags', 'imageTags0', 'imageTags1', 'iframeTags'];

	// Check every Style tag:
	for (var i = 0; i < hvvStyleTags.length; i++) {

		// The ID of the style tag related to the set of elements:
		var $hvvStyleTag = $('#' + hvvStyleTags[i]);

		// If the ID exist:
		if ($hvvStyleTag.length > 0) {
			// Insert the set of elements flag into the response object:
			hvvLoadObjs.push(hvvStyleTags[i]);
		}
	}

	// -------------------
	// 4) Add show ID an Class flag to reponse object:
	// ------------------

	// Check if showIdClass is set:
	if (showIdClass) {
		hvvLoadObjs.push('showIdClass');
	} else {
		// Check if showIdClass is set:
		if (showId) {
			hvvLoadObjs.push('showId');
		}

		// Check if showIdClass is set:
		if (showClass) {
			hvvLoadObjs.push('showClass');
		}
	}

	// Return the response object:
	return hvvLoadObjs;
}

// Remove labels:
function hvvRemoveDisplay(tagType) {
	// Get style tag block by id:
	var $styleTag = $('#' + tagType);

	// Check if stule bloc exist...
	if ($styleTag.length > 0) {
		// ... and remove:
		$styleTag.remove();
	}

	// Get specific div tag by specific label:
	var hvvClassType = 'hvv-tagInfo' + tagType;
	var $hvvTagInfo = $('.' + hvvClassType);

	// Chek if div tag exist...
	if ($hvvTagInfo.length > 0) {
		// ...and remove:
		$hvvTagInfo.remove();
	}
}



//----------------------
// Dom traversing:
//----------------------
var domTreeList = "include";
var domTagList = [];
var domElementList = [];

var stringTab = "&nbsp;&nbsp;&nbsp;&nbsp;";
var startOpenTag = "&lt;";
var startCloseTag = "&lt;/";
var endTag = "&gt;";

//var stringTab = "    ";
//var startOpenTag = "<";
//var startCloseTag = "</";
//var endTag = ">";

function hvvDomTree(domNode, oldTabLevel){
	
	// Get child nodes:
	var domNodeChildList = domNode.children;
	
	// If the element has a "#shadow-root":
	domNodeChildList = domNode.shadowRoot == null ? domNodeChildList : domNode.shadowRoot.children;
	
	// If the element has a "#document-fragment":
	domNodeChildList = domNode.content == undefined ? domNodeChildList : domNode.content.nodeName == "#document-fragment" ? domNode.content.children : domNodeChildList;

	var domNodeChildListLength = domNodeChildList.length;
	
	// If has nodes:
	if(domNodeChildListLength > 0){
		
		// Get each node:
		for(var i = 0; i < domNodeChildListLength; i++){
			
			// Get node element and its tag name:
			var domNodeChild = domNodeChildList[i];
			var domNodeChildName = domNodeChild.tagName;
			var domNodeChildAttributeList = domNodeChild.getAttributeNames();
			var domNodeChildAttributes = domNodeChildAttributeList.map(function(k) { return " " + k + '="' + domNodeChild.attributes[k].value.replace('<', '&lt;').replace('>', '&gt;') + '"' }).join(' ');;
				
			var myTagName = domNodeChildName.toLowerCase();
			
			// Add tag name to array of tags:
			if(domTagList.indexOf(myTagName) == -1){
				domTagList.push(myTagName);
			}

			// Begin of line, with "span" of line number and tab levels:
			var tabRoot = 0;
			var tabLevelString = '';
			tabLevel = oldTabLevel + 1;
			
			// Level of tabs:
			while(tabRoot < tabLevel){
				tabLevelString += stringTab;
				tabRoot++;
			}

			// Open/Colse tags:
			var openTag = startOpenTag + myTagName + domNodeChildAttributes + endTag;
			var colseTag = startCloseTag + myTagName + endTag;

			// Self-closing tags:
			switch(myTagName){
				case 'area' :
				case 'base' :
				case 'br' :
				case 'col' :
				case 'embed' :
				case 'hr' :
				case 'img' :
				case 'input' :
				case 'link' :
				case 'meta' :
				case 'param' :
				case 'source' :
				case 'track' :
				case 'wbr' :
					colseTag = '';
					break;
			}
			
			var domTreeElement = "";

			var color = "";

			switch(myTagName){
				case 'header':
					color = html5Color[0];
					break;
				case 'nav':
					color = html5Color[1];
					break;
				case 'main':
					color = html5Color[2];
					break;
				case 'section':
					color = html5Color[3];
					break;
				case 'footer':
					color = html5Color[4];
					break;
				case 'div':
					color = generalColor[0];
					break;
				case 'span':
					color = generalColor[1];
					break;
				case 'h1':
					color = headingColor[0];
					break;
				case 'h2':
					color = headingColor[1];
					break;
				case 'h3':
					color = headingColor[2];
					break;
				case 'h4':
					color = headingColor[3];
					break;
				case 'h5':
					color = headingColor[4];
					break;
				case 'h6':
					color = headingColor[5];
					break;
				case 'p':
					color = textColor[0];
					break;
				case 'br':
					color = textColor[1];
					break;
				case 'strong':
					color = textColor[2];
					break;
				case 'b':
					color = textColor[3];
					break;
				case 'em':
					color = textColor[4];
					break;
				case 'i':
					color = textColor[5];
					break;
				case 'ul':
					color = listColor[0];
					break;
				case 'ol':
					color = listColor[1];
					break;
				case 'li':
					color = listColor[2];
					break;
				case 'a':
					color = anchorColor[0];
					break;
				case 'img':
					color = imageColor[0];
					break;
				case 'picture':
					color = imageColor[1];
					break;
				case 'iframe':
					color = iframeColor[1];
					break;
				default:
					color = "#999";
					break;
			}

			var domElementListLength = domElementList.length;
			
			domElementList.push(domNodeChild);
			
			var domTreeNumber = '<li><span class="hvv-domTree-number"></span>';
			
			var tagAnchor = '<a href="#" class="hvv-domtree-node hvv-domtree-node-' + myTagName + ' hvv-domtree-node-defaultcolor" data-hvvDomChildIndex="' + domElementListLength + '" style="color:' + color + '">';

			var include1 = '';
			// If child has child to, insert "include" inside the tag:
			if(domNodeChild.children.length > 0){
				//include1 = '</a><br>' + 'include' + '<br>' + domTreeNumber + tagAnchor + tabLevelString;
				include1 = '</a></li>' + 'include' + domTreeNumber + tagAnchor + tabLevelString;
			}

			//var include2 = '<br> include';
			var include2 = '</li> include';
			// If last child, dont break line and dont insert "include" after the tag:
			if(i == domNodeChildListLength-1){
				include2 = '';
			}

			domTreeElement = domTreeNumber + tagAnchor + tabLevelString + openTag + include1 + colseTag + '</a>' + include2;
			
			//console.log(domTreeElement);
			
			domTreeList = domTreeList.replace('include', domTreeElement);

			//console.log(domTreeList);
			
			// Traverse child nodes:
			hvvDomTree(domNodeChild, tabLevel);		
		}
	}

	return [domTagList, domTreeList];
}

function scrollToElement(index){
	var domElement = domElementList[index];
	var domElementTagName = domElement.tagName.toLowerCase();
	
	// Scroll into view:
	domElement.scrollIntoView({ behavior: 'smooth', block: 'center' });

	// Remove hover class from any previous element:
	$('.hvv-tagInfo-hover').removeClass('hvv-tagInfo-hover');
	
	// Add hover class on selected element:
	switch(domElementTagName){
		case 'img':
		case 'br':
			$(domElement).next('.hvv-tagInfo' + domElementTagName).addClass('hvv-tagInfo-hover');
			break;
		default:
			$(domElement).children('.hvv-tagInfo' + domElementTagName).addClass('hvv-tagInfo-hover');
	}
}



//----------------------
// Message:
//----------------------

// Recives message from popup.js:
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

	// Check value to trigger action of specific tags or attribute:
	switch (request.hvvDisplayObj) {

		case "idClass":
			showId = true;
			hvvShowId();
			showClass = true;
			hvvShowClass();
			showIdClass = true;
			break;
		case "idClassRemove":
			showId = false;
			hvvShowId();
			showClass = false;
			hvvShowClass();
			showIdClass = false
			break;

		case "id":
			showId = true;
			hvvShowId();
			break;
		case "idRemove":
			showId = false;
			hvvShowId();
			break;

		case "class":
			showClass = true;
			hvvShowClass();
			break;
		case "classRemove":
			showClass = false;
			hvvShowClass();
			break;

		// -------------------------
		// 
		//  If outline tag:
		//  If its a block action, remove all individual tags first, then create aganin. Prevent duplicates.
		//  Block of tags or specific tag;
		//  Append label of specific tag and color styles;
		//  
		//  If remove outline:
		//  Remove all outlines.
		// 
		// -------------------------

		// ----------------------
		// Heading tags:
		// ----------------------
		case "headingTags":
			hvvRemoveDisplay('headingTags0');
			hvvRemoveDisplay('headingTags1');
			hvvRemoveDisplay('headingTags2');
			hvvRemoveDisplay('headingTags3');
			hvvRemoveDisplay('headingTags4');
			hvvRemoveDisplay('headingTags5');
			hvvDisplay('headingTags', headingColor);
			break;
		case "headingTagsRemove":
			hvvRemoveDisplay('headingTags');
			break;

		case "headingTags0":
			headingTags0[0] = headingTags[0];
			hvvDisplay('headingTags0', headingColor[0]);
			break;
		case "headingTags0Remove":
			hvvRemoveDisplay('headingTags0');
			break;

		case "headingTags1":
			headingTags1[0] = headingTags[1];
			hvvDisplay('headingTags1', headingColor[1]);
			break;
		case "headingTags1Remove":
			hvvRemoveDisplay('headingTags1');
			break;

		case "headingTags2":
			headingTags2[0] = headingTags[2];
			hvvDisplay('headingTags2', headingColor[2]);
			break;
		case "headingTags2Remove":
			hvvRemoveDisplay('headingTags2');
			break;

		case "headingTags3":
			headingTags3[0] = headingTags[3];
			hvvDisplay('headingTags3', headingColor[3]);
			break;
		case "headingTags3Remove":
			hvvRemoveDisplay('headingTags3');
			break;

		case "headingTags4":
			headingTags4[0] = headingTags[4];
			hvvDisplay('headingTags4', headingColor[4]);
			break;
		case "headingTags4Remove":
			hvvRemoveDisplay('headingTags4');
			break;

		case "headingTags5":
			headingTags5[0] = headingTags[5];
			hvvDisplay('headingTags5', headingColor[5]);
			break;
		case "headingTags5Remove":
			hvvRemoveDisplay('headingTags5');
			break;

		// ----------------------
		// HTML5 tags:
		// ----------------------

		case "html5Tags":
			hvvRemoveDisplay('html5Tags0');
			hvvRemoveDisplay('html5Tags1');
			hvvRemoveDisplay('html5Tags2');
			hvvRemoveDisplay('html5Tags3');
			hvvRemoveDisplay('html5Tags4');
			hvvDisplay('html5Tags', html5Color);
			break;
		case "html5TagsRemove":
			hvvRemoveDisplay('html5Tags');
			break;

		case "html5Tags0":
			html5Tags0[0] = html5Tags[0];
			hvvDisplay('html5Tags0', html5Color[0]);
			break;
		case "html5Tags0Remove":
			hvvRemoveDisplay('html5Tags0');
			break;

		case "html5Tags1":
			html5Tags1[0] = html5Tags[1];
			hvvDisplay('html5Tags1', html5Color[1]);
			break;
		case "html5Tags1Remove":
			hvvRemoveDisplay('html5Tags1');
			break;

		case "html5Tags2":
			html5Tags2[0] = html5Tags[2];
			hvvDisplay('html5Tags2', html5Color[2]);
			break;
		case "html5Tags2Remove":
			hvvRemoveDisplay('html5Tags2');
			break;

		case "html5Tags3":
			html5Tags3[0] = html5Tags[3];
			hvvDisplay('html5Tags3', html5Color[3]);
			break;
		case "html5Tags3Remove":
			hvvRemoveDisplay('html5Tags3');
			break;

		case "html5Tags4":
			html5Tags4[0] = html5Tags[4];
			hvvDisplay('html5Tags4', html5Color[4]);
			break;
		case "html5Tags4Remove":
			hvvRemoveDisplay('html5Tags4');
			break;

		// ----------------------
		// General tags:
		// ----------------------
		case "generalTags":
			hvvRemoveDisplay('generalTags0');
			hvvRemoveDisplay('generalTags1');
			hvvDisplay('generalTags', generalColor);
			break;
		case "generalTagsRemove":
			hvvRemoveDisplay('generalTags');
			break;

		case "generalTags0":
			generalTags0[0] = generalTags[0];
			hvvDisplay('generalTags0', generalColor[0]);
			break;
		case "generalTags0Remove":
			hvvRemoveDisplay('generalTags0');
			break;

		case "generalTags1":
			generalTags1[0] = generalTags[1];
			hvvDisplay('generalTags1', generalColor[1]);
			break;
		case "generalTags1Remove":
			hvvRemoveDisplay('generalTags1');
			break;

		// ----------------------
		// Text tags:
		// ----------------------
		case "textTags":
			hvvRemoveDisplay('textTags0');
			hvvRemoveDisplay('textTags1');
			hvvRemoveDisplay('textTags2');
			hvvRemoveDisplay('textTags3');
			hvvRemoveDisplay('textTags4');
			hvvRemoveDisplay('textTags5');
			hvvDisplay('textTags', textColor);
			break;
		case "textTagsRemove":
			hvvRemoveDisplay('textTags');
			break;

		case "textTags0":
			textTags0[0] = textTags[0];
			hvvDisplay('textTags0', textColor[0]);
			break;
		case "textTags0Remove":
			hvvRemoveDisplay('textTags0');
			break;

		case "textTags1":
			textTags1[0] = textTags[1];
			hvvDisplay('textTags1', textColor[1]);
			break;
		case "textTags1Remove":
			hvvRemoveDisplay('textTags1');
			break;

		case "textTags2":
			textTags2[0] = textTags[2];
			hvvDisplay('textTags2', textColor[2]);
			break;
		case "textTags2Remove":
			hvvRemoveDisplay('textTags2');
			break;

		case "textTags3":
			textTags3[0] = textTags[3];
			hvvDisplay('textTags3', textColor[3]);
			break;
		case "textTags3Remove":
			hvvRemoveDisplay('textTags3');
			break;

		case "textTags4":
			textTags4[0] = textTags[4];
			hvvDisplay('textTags4', textColor[4]);
			break;
		case "textTags4Remove":
			hvvRemoveDisplay('textTags4');
			break;

		case "textTags5":
			textTags5[0] = textTags[5];
			hvvDisplay('textTags5', textColor[5]);
			break;
		case "textTags5Remove":
			hvvRemoveDisplay('textTags5');
			break;

		// ----------------------
		// List tags:
		// ----------------------
		case "listTags":
			hvvRemoveDisplay('listTags0');
			hvvRemoveDisplay('listTags1');
			hvvRemoveDisplay('listTags2');
			hvvDisplay('listTags', listColor);
			break;
		case "listTagsRemove":
			hvvRemoveDisplay('listTags');
			break;

		case "listTags0":
			listTags0[0] = listTags[0];
			hvvDisplay('listTags0', listColor[0]);
			break;
		case "listTags0Remove":
			hvvRemoveDisplay('listTags0');
			break;

		case "listTags1":
			listTags1[0] = listTags[1];
			hvvDisplay('listTags1', listColor[1]);
			break;
		case "listTags1Remove":
			hvvRemoveDisplay('listTags1');
			break;

		case "listTags2":
			listTags2[0] = listTags[2];
			hvvDisplay('listTags2', listColor[2]);
			break;
		case "listTags2Remove":
			hvvRemoveDisplay('listTags2');
			break;

		// ----------------------
		// Anchor tags:
		// ----------------------
		case "anchorTags":
			hvvDisplay('anchorTags', anchorColor);
			break;
		case "anchorTagsRemove":
			hvvRemoveDisplay('anchorTags');
			break;

		// ----------------------
		// Image tags:
		// ----------------------
		case "imageTags":
			hvvRemoveDisplay('imageTags0');
			hvvRemoveDisplay('imageTags1');
			hvvDisplay('imageTags', imageColor);
			break;
		case "imageTagsRemove":
			hvvRemoveDisplay('imageTags');
			break;

		case "imageTags0":
			imageTags0[0] = imageTags[0];
			hvvDisplay('imageTags0', imageColor[0]);
			break;
		case "imageTags0Remove":
			hvvRemoveDisplay('imageTags0');
			break;

		case "imageTags1":
			imageTags1[0] = imageTags[1];
			hvvDisplay('imageTags1', imageColor[1]);
			break;
		case "imageTags1Remove":
			hvvRemoveDisplay('imageTags1');
			break;

		// ----------------------
		// Iframe tags:
		// ----------------------
		case "iframeTags":
			hvvDisplay('iframeTags', iframeColor);
			break;
		case "iframeTagsRemove":
			hvvRemoveDisplay('iframeTags');
			break;
	}

	// Message received when open extension menu:
	if (request.hvvLoadActionsObj == 'check') {		
		// Send to popup.js:
		// 1) Title and Description of the page
		// 2) Array of Dom elements
		// 3) Any tag outlined
		// 4) Show ID an Class flag
		sendResponse({ status: hvvLoadActions() });
	}

	if (request.hvvScrollToObj){
		// console.log('hvvScrollToObj', request.hvvScrollToObj);
		var nodeIndex = Number(request.hvvScrollToObj);
		scrollToElement(nodeIndex);
	}

	return true;
});