from django.shortcuts import render , redirect
from .api import *
from json import dumps
import requests
from datetime import datetime, timezone

# Create your views here.

def home(request):
    date = Covid19.objects.get(country='World')
    now = datetime.now(timezone.utc)
    dif = now - date.updated_on
    hour = dif.seconds / 3600
    if hour > 1.5:
        start_scheduler()
    else:
        pass    
    return redirect('covid', country='World')

def covid(request,country):
	cov = Covid19.objects.all().order_by('-confirmed').exclude(pk=420)
	world = Covid19.objects.get(country=country)
	data = {}
	data2 = []
	codes = [{"name":"Afghanistan","alpha2":"AF","country-code":"004"},{"name":"Åland Islands","alpha2":"AX","country-code":"248"},{"name":"Albania","alpha2":"AL","country-code":"008"},{"name":"Algeria","alpha2":"DZ","country-code":"012"},{"name":"American Samoa","alpha2":"AS","country-code":"016"},{"name":"Andorra","alpha2":"AD","country-code":"020"},{"name":"Angola","alpha2":"AO","country-code":"024"},{"name":"Anguilla","alpha2":"AI","country-code":"660"},{"name":"Antarctica","alpha2":"AQ","country-code":"010"},{"name":"Antigua and Barbuda","alpha2":"AG","country-code":"028"},{"name":"Argentina","alpha2":"AR","country-code":"032"},{"name":"Armenia","alpha2":"AM","country-code":"051"},{"name":"Aruba","alpha2":"AW","country-code":"533"},{"name":"Australia","alpha2":"AU","country-code":"036"},{"name":"Austria","alpha2":"AT","country-code":"040"},{"name":"Azerbaijan","alpha2":"AZ","country-code":"031"},{"name":"Bahamas","alpha2":"BS","country-code":"044"},{"name":"Bahrain","alpha2":"BH","country-code":"048"},{"name":"Bangladesh","alpha2":"BD","country-code":"050"},{"name":"Barbados","alpha2":"BB","country-code":"052"},{"name":"Belarus","alpha2":"BY","country-code":"112"},{"name":"Belgium","alpha2":"BE","country-code":"056"},{"name":"Belize","alpha2":"BZ","country-code":"084"},{"name":"Benin","alpha2":"BJ","country-code":"204"},{"name":"Bermuda","alpha2":"BM","country-code":"060"},{"name":"Bhutan","alpha2":"BT","country-code":"064"},{"name":"Bolivia","alpha2":"BO","country-code":"068"},{"name":"Bonaire, Sint Eustatius and Saba","alpha2":"BQ","country-code":"535"},{"name":"Bosnia and Herzegovina","alpha2":"BA","country-code":"070"},{"name":"Bosnia and Herzegovina","alpha2":"BA","country-code":"070"},{"name":"Botswana","alpha2":"BW","country-code":"072"},{"name":"Bouvet Island","alpha2":"BV","country-code":"074"},{"name":"Brazil","alpha2":"BR","country-code":"076"},{"name":"British Indian Ocean Territory","alpha2":"IO","country-code":"086"},{"name":"Brunei","alpha2":"BN","country-code":"096"},{"name":"Bulgaria","alpha2":"BG","country-code":"100"},{"name":"Burkina Faso","alpha2":"BF","country-code":"854"},{"name":"Burundi","alpha2":"BI","country-code":"108"},{"name":"Cabo Verde","alpha2":"CV","country-code":"132"},{"name":"Cambodia","alpha2":"KH","country-code":"116"},{"name":"Cameroon","alpha2":"CM","country-code":"120"},{"name":"Canada","alpha2":"CA","country-code":"124"},{"name":"Cayman Islands","alpha2":"KY","country-code":"136"},{"name":"Central African Republic","alpha2":"CF","country-code":"140"},{"name":"Chad","alpha2":"TD","country-code":"148"},{"name":"Chile","alpha2":"CL","country-code":"152"},{"name":"China","alpha2":"CN","country-code":"156"},{"name":"Christmas Island","alpha2":"CX","country-code":"162"},{"name":"Cocos (Keeling) Islands","alpha2":"CC","country-code":"166"},{"name":"Colombia","alpha2":"CO","country-code":"170"},{"name":"Comoros","alpha2":"KM","country-code":"174"},{"name":"Congo Republic","alpha2":"CG","country-code":"178"},{"name":"DR Congo","alpha2":"CD","country-code":"180"},{"name":"Cook Islands","alpha2":"CK","country-code":"184"},{"name":"Costa Rica","alpha2":"CR","country-code":"188"},{"name":"Cote d'Ivoire","alpha2":"CI","country-code":"384"},{"name":"Ivory Coast","alpha2":"CI","country-code":"384"},{"name":"Croatia","alpha2":"HR","country-code":"191"},{"name":"Cuba","alpha2":"CU","country-code":"192"},{"name":"Curaçao","alpha2":"CW","country-code":"531"},{"name":"Cyprus","alpha2":"CY","country-code":"196"},{"name":"Czechia","alpha2":"CZ","country-code":"203"},{"name":"Czechia","alpha2":"CZ","country-code":"203"},{"name":"Denmark","alpha2":"DK","country-code":"208"},{"name":"Djibouti","alpha2":"DJ","country-code":"262"},{"name":"Dominica","alpha2":"DM","country-code":"212"},{"name":"Dominican Republic","alpha2":"DO","country-code":"214"},{"name":"Ecuador","alpha2":"EC","country-code":"218"},{"name":"Egypt","alpha2":"EG","country-code":"818"},{"name":"El Salvador","alpha2":"SV","country-code":"222"},{"name":"Equatorial Guinea","alpha2":"GQ","country-code":"226"},{"name":"Eritrea","alpha2":"ER","country-code":"232"},{"name":"Estonia","alpha2":"EE","country-code":"233"},{"name":"Eswatini","alpha2":"SZ","country-code":"748"},{"name":"Ethiopia","alpha2":"ET","country-code":"231"},{"name":"Falkland Island","alpha2":"FK","country-code":"238"},{"name":"Faroe Islands","alpha2":"FO","country-code":"234"},{"name":"Fiji","alpha2":"FJ","country-code":"242"},{"name":"Finland","alpha2":"FI","country-code":"246"},{"name":"France","alpha2":"FR","country-code":"250"},{"name":"French Guiana","alpha2":"GF","country-code":"254"},{"name":"French Polynesia","alpha2":"PF","country-code":"258"},{"name":"French Southern Territories","alpha2":"TF","country-code":"260"},{"name":"Gabon","alpha2":"GA","country-code":"266"},{"name":"Gambia","alpha2":"GM","country-code":"270"},{"name":"Georgia","alpha2":"GE","country-code":"268"},{"name":"Germany","alpha2":"DE","country-code":"276"},{"name":"Ghana","alpha2":"GH","country-code":"288"},{"name":"Gibraltar","alpha2":"GI","country-code":"292"},{"name":"Greece","alpha2":"GR","country-code":"300"},{"name":"Greenland","alpha2":"GL","country-code":"304"},{"name":"Grenada","alpha2":"GD","country-code":"308"},{"name":"Guadeloupe","alpha2":"GP","country-code":"312"},{"name":"Guam","alpha2":"GU","country-code":"316"},{"name":"Guatemala","alpha2":"GT","country-code":"320"},{"name":"Guernsey","alpha2":"GG","country-code":"831"},{"name":"Guinea","alpha2":"GN","country-code":"324"},{"name":"Guinea-Bissau","alpha2":"GW","country-code":"624"},{"name":"Guyana","alpha2":"GY","country-code":"328"},{"name":"Haiti","alpha2":"HT","country-code":"332"},{"name":"Heard Island and McDonald Islands","alpha2":"HM","country-code":"334"},{"name":"Holy See","alpha2":"VA","country-code":"336"},{"name":"Honduras","alpha2":"HN","country-code":"340"},{"name":"Hong Kong","alpha2":"HK","country-code":"344"},{"name":"Hungary","alpha2":"HU","country-code":"348"},{"name":"Iceland","alpha2":"IS","country-code":"352"},{"name":"India","alpha2":"IN","country-code":"356"},{"name":"Indonesia","alpha2":"ID","country-code":"360"},{"name":"Iran","alpha2":"IR","country-code":"364"},{"name":"Iraq","alpha2":"IQ","country-code":"368"},{"name":"Ireland","alpha2":"IE","country-code":"372"},{"name":"Isle of Man","alpha2":"IM","country-code":"833"},{"name":"Israel","alpha2":"IL","country-code":"376"},{"name":"Italy","alpha2":"IT","country-code":"380"},{"name":"Jamaica","alpha2":"JM","country-code":"388"},{"name":"Japan","alpha2":"JP","country-code":"392"},{"name":"Jersey","alpha2":"JE","country-code":"832"},{"name":"Jordan","alpha2":"JO","country-code":"400"},{"name":"Kazakhstan","alpha2":"KZ","country-code":"398"},{"name":"Kenya","alpha2":"KE","country-code":"404"},{"name":"Kiribati","alpha2":"KI","country-code":"296"},{"name":"Korea, North","alpha2":"KP","country-code":"408"},{"name":"S. Korea","alpha2":"KR","country-code":"410"},{"name":"North Korea","alpha2":"KP","country-code":"408"},{"name":"Korea, South","alpha2":"KR","country-code":"410"},{"name":"Kuwait","alpha2":"KW","country-code":"414"},{"name":"Kyrgyzstan","alpha2":"KG","country-code":"417"},{"name":"Laos","alpha2":"LA","country-code":"418"},{"name":"Latvia","alpha2":"LV","country-code":"428"},{"name":"Lebanon","alpha2":"LB","country-code":"422"},{"name":"Lesotho","alpha2":"LS","country-code":"426"},{"name":"Liberia","alpha2":"LR","country-code":"430"},{"name":"Libya","alpha2":"LY","country-code":"434"},{"name":"Liechtenstein","alpha2":"LI","country-code":"438"},{"name":"Lithuania","alpha2":"LT","country-code":"440"},{"name":"Luxembourg","alpha2":"LU","country-code":"442"},{"name":"Macao","alpha2":"MO","country-code":"446"},{"name":"Madagascar","alpha2":"MG","country-code":"450"},{"name":"Malawi","alpha2":"MW","country-code":"454"},{"name":"Malaysia","alpha2":"MY","country-code":"458"},{"name":"Maldives","alpha2":"MV","country-code":"462"},{"name":"Mali","alpha2":"ML","country-code":"466"},{"name":"Malta","alpha2":"MT","country-code":"470"},{"name":"Marshall Islands","alpha2":"MH","country-code":"584"},{"name":"Martinique","alpha2":"MQ","country-code":"474"},{"name":"Mauritania","alpha2":"MR","country-code":"478"},{"name":"Mauritius","alpha2":"MU","country-code":"480"},{"name":"Mayotte","alpha2":"YT","country-code":"175"},{"name":"Mexico","alpha2":"MX","country-code":"484"},{"name":"Micronesia (Federated States of)","alpha2":"FM","country-code":"583"},{"name":"Moldova","alpha2":"MD","country-code":"498"},{"name":"Monaco","alpha2":"MC","country-code":"492"},{"name":"Mongolia","alpha2":"MN","country-code":"496"},{"name":"Montenegro","alpha2":"ME","country-code":"499"},{"name":"Montserrat","alpha2":"MS","country-code":"500"},{"name":"Morocco","alpha2":"MA","country-code":"504"},{"name":"Mozambique","alpha2":"MZ","country-code":"508"},{"name":"Myanmar","alpha2":"MM","country-code":"104"},{"name":"Namibia","alpha2":"NA","country-code":"516"},{"name":"Nauru","alpha2":"NR","country-code":"520"},{"name":"Nepal","alpha2":"NP","country-code":"524"},{"name":"Netherlands","alpha2":"NL","country-code":"528"},{"name":"New Caledonia","alpha2":"NC","country-code":"540"},{"name":"New Zealand","alpha2":"NZ","country-code":"554"},{"name":"Nicaragua","alpha2":"NI","country-code":"558"},{"name":"Niger","alpha2":"NE","country-code":"562"},{"name":"Nigeria","alpha2":"NG","country-code":"566"},{"name":"Niue","alpha2":"NU","country-code":"570"},{"name":"Norfolk Island","alpha2":"NF","country-code":"574"},{"name":"North Macedonia","alpha2":"MK","country-code":"807"},{"name":"Northern Mariana Islands","alpha2":"MP","country-code":"580"},{"name":"Norway","alpha2":"NO","country-code":"578"},{"name":"Oman","alpha2":"OM","country-code":"512"},{"name":"Pakistan","alpha2":"PK","country-code":"586"},{"name":"Palau","alpha2":"PW","country-code":"585"},{"name":"Palestine","alpha2":"PS","country-code":"275"},{"name":"Panama","alpha2":"PA","country-code":"591"},{"name":"Papua New Guinea","alpha2":"PG","country-code":"598"},{"name":"Paraguay","alpha2":"PY","country-code":"600"},{"name":"Peru","alpha2":"PE","country-code":"604"},{"name":"Philippines","alpha2":"PH","country-code":"608"},{"name":"Pitcairn","alpha2":"PN","country-code":"612"},{"name":"Poland","alpha2":"PL","country-code":"616"},{"name":"Portugal","alpha2":"PT","country-code":"620"},{"name":"Puerto Rico","alpha2":"PR","country-code":"630"},{"name":"Qatar","alpha2":"QA","country-code":"634"},{"name":"Reunion","alpha2":"RE","country-code":"638"},{"name":"Romania","alpha2":"RO","country-code":"642"},{"name":"Russia","alpha2":"RU","country-code":"643"},{"name":"Rwanda","alpha2":"RW","country-code":"646"},{"name":"St. Barth","alpha2":"BL","country-code":"652"},{"name":"Saint Helena, Ascension and Tristan da Cunha","alpha2":"SH","country-code":"654"},{"name":"Saint Kitts and Nevis","alpha2":"KN","country-code":"659"},{"name":"Saint Lucia","alpha2":"LC","country-code":"662"},{"name":"Saint Martin","alpha2":"MF","country-code":"663"},{"name":"Saint Pierre Miquelon","alpha2":"PM","country-code":"666"},{"name":"St. Vincent Grenadines","alpha2":"VC","country-code":"670"},{"name":"Samoa","alpha2":"WS","country-code":"882"},{"name":"San Marino","alpha2":"SM","country-code":"674"},{"name":"Sao Tome and Principe","alpha2":"ST","country-code":"678"},{"name":"Saudi Arabia","alpha2":"SA","country-code":"682"},{"name":"Senegal","alpha2":"SN","country-code":"686"},{"name":"Serbia","alpha2":"RS","country-code":"688"},{"name":"Seychelles","alpha2":"SC","country-code":"690"},{"name":"Sierra Leone","alpha2":"SL","country-code":"694"},{"name":"Singapore","alpha2":"SG","country-code":"702"},{"name":"Sint Maarten","alpha2":"SX","country-code":"534"},{"name":"Slovakia","alpha2":"SK","country-code":"703"},{"name":"Slovenia","alpha2":"SI","country-code":"705"},{"name":"Solomon Islands","alpha2":"SB","country-code":"090"},{"name":"Somalia","alpha2":"SO","country-code":"706"},{"name":"South Africa","alpha2":"ZA","country-code":"710"},{"name":"South Georgia and the South Sandwich Islands","alpha2":"GS","country-code":"239"},{"name":"South Sudan","alpha2":"SS","country-code":"728"},{"name":"Spain","alpha2":"ES","country-code":"724"},{"name":"Sri Lanka","alpha2":"LK","country-code":"144"},{"name":"Sudan","alpha2":"SD","country-code":"729"},{"name":"Suriname","alpha2":"SR","country-code":"740"},{"name":"Svalbard and Jan Mayen","alpha2":"SJ","country-code":"744"},{"name":"Sweden","alpha2":"SE","country-code":"752"},{"name":"Switzerland","alpha2":"CH","country-code":"756"},{"name":"Syria","alpha2":"SY","country-code":"760"},{"name":"Taiwan","alpha2":"TW","country-code":"158"},{"name":"Tajikistan","alpha2":"TJ","country-code":"762"},{"name":"Tanzania","alpha2":"TZ","country-code":"834"},{"name":"Thailand","alpha2":"TH","country-code":"764"},{"name":"Timor-Leste","alpha2":"TL","country-code":"626"},{"name":"Togo","alpha2":"TG","country-code":"768"},{"name":"Tokelau","alpha2":"TK","country-code":"772"},{"name":"Tonga","alpha2":"TO","country-code":"776"},{"name":"Trinidad and Tobago","alpha2":"TT","country-code":"780"},{"name":"Tunisia","alpha2":"TN","country-code":"788"},{"name":"Turkey","alpha2":"TR","country-code":"792"},{"name":"Turkmenistan","alpha2":"TM","country-code":"795"},{"name":"Turks and Caicos","alpha2":"TC","country-code":"796"},{"name":"Tuvalu","alpha2":"TV","country-code":"798"},{"name":"Uganda","alpha2":"UG","country-code":"800"},{"name":"Ukraine","alpha2":"UA","country-code":"804"},{"name":"UAE","alpha2":"AE","country-code":"784"},{"name":"UK","alpha2":"GB","country-code":"826"},{"name":"USA","alpha2":"US","country-code":"840"},{"name":"United States of America","alpha2":"US","country-code":"840"},{"name":"United States Minor Outlying Islands","alpha2":"UM","country-code":"581"},{"name":"Uruguay","alpha2":"UY","country-code":"858"},{"name":"Uzbekistan","alpha2":"UZ","country-code":"860"},{"name":"Vanuatu","alpha2":"VU","country-code":"548"},{"name":"Venezuela","alpha2":"VE","country-code":"862"},{"name":"Vietnam","alpha2":"VN","country-code":"704"},{"name":"British Virgin Islands","alpha2":"VG","country-code":"092"},{"name":"Virgin Islands (U.S.)","alpha2":"VI","country-code":"850"},{"name":"Wallis and Futuna","alpha2":"WF","country-code":"876"},{"name":"Western Sahara","alpha2":"EH","country-code":"732"},{"name":"Yemen","alpha2":"YE","country-code":"887"},{"name":"Zambia","alpha2":"ZM","country-code":"894"},{"name":"Zimbabwe","alpha2":"ZW","country-code":"716"}]
	
	for i in cov:
		for s in codes:
			if s["name"] == i.country:
				data[s['alpha2']] = i.confirmed
	datajson = dumps(data)
	data2.append(world.deaths)
	data2.append(world.active)
	data2.append(world.recovered)
	d2json = dumps(data2)
	
	return render(request, 'dashboard.html', {'data':datajson,'covid20':cov,"world":world,"data2":d2json})