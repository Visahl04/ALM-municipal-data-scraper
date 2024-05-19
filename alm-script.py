import requests, pandas as pd
from bs4 import BeautifulSoup
from lxml import etree


data = []

def first_req():

    url = "https://alm.imiscloud.com/ALALM/ALALM/About/ALM-Municipal-Directory.aspx"

    payload = {}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8,hi;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'ASP.NET_SessionId=pe0kt4kduxxu5hd3arfyonp0; __RequestVerificationToken=hemRMm5w0tjsbRUI1Gx6VNIKs4INQr7ScObH9vFZVCQOfQR2tEUw0rNAsUXnoBbLLVS88b2wLJmsl0ugyA1sMhT9_zYSLN8SWFNglW8DDQ41; __RequestVerificationToken=hemRMm5w0tjsbRUI1Gx6VNIKs4INQr7ScObH9vFZVCQOfQR2tEUw0rNAsUXnoBbLLVS88b2wLJmsl0ugyA1sMhT9_zYSLN8SWFNglW8DDQ41',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.st)
    return response



def second_requesting(q,no):

    viewstate = q[0]
    token = q[1]
    url = f"https://alm.imiscloud.com/ALALM/ALALM/About/ALM-Municipal-Directory.aspx?WebsiteKey={q[2]}"
    print(url)
    
    payload = f"ctl01%24ScriptManager1=ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ListerPanel%7Cctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Grid1%24ctl00%24ctl03%24ctl01%24ctl{no}&__WPPS=s&__CTRLKEY=&__SHIFTKEY=&ctl01_ScriptManager1_TSM=%3B%3BAjaxControlToolkit%3Aen-US%3A0c8c847b-b611-49a7-8e75-2196aa6e72fa%3Aea597d4b%3Ab25378d2%3BTelerik.Web.UI%2C%20Version%3D2023.1.117.45%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D121fae78165ba3d4%3Aen-US%3Aba768a1f-3205-4bbb-b2c9-b540445080b3%3A16e4e7cd%3A33715776%3Af7645509%3A24ee1bba%3Ae330518b%3A2003d0b8%3Ac128760b%3A88144a7a%3A1e771326%3Ac8618e41%3A1a73651d%3A333f8d94%3A58366029%3Af46195d3%3Aaa288e2d%3Ab092aa46%3Ae524c98b%3Aed16cbdc%3Ab2e06756%3A92fe8ea0%3Afa31b949%3A4877f69a%3A19620875%3A874f8ea2%3A490a9d4e%3Abd8f85e4%3B&NavMenuClientID=ctl01_ciPrimaryNavigation_NavControl_NavMenu&ctl01%24lastClickedElementId=&ctl01_ciPrimaryNavigation_NavControl_NavMenu_ClientState=&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Sheet0%24ctl01=59f8d114-2158-496f-abb4-7d3ba9d69a98.FS1.FL13&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Sheet0%24Input0%24TextBox1=&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Sheet0%24ctl04=59f8d114-2158-496f-abb4-7d3ba9d69a98.FS1.FL8&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Sheet0%24Input1%24ctl03%24TextBox1=&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Sheet0%24Input1%24ctl06%24TextBox1=&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Sheet0%24ctl07=59f8d114-2158-496f-abb4-7d3ba9d69a98.FS1.FL11&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Sheet0%24Input2%24DropDown1=&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Sheet0%24ctl10=59f8d114-2158-496f-abb4-7d3ba9d69a98.FS1.FL10&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24HiddenKeyField1=code_ID&ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Grid1%24ctl00%24ctl03%24ctl01%24PageSizeComboBox=20&ctl01_TemplateBody_WebPartManager1_gwpciNewQueryMenuCommon_ciNewQueryMenuCommon_ResultsGrid_Grid1_ctl00_ctl03_ctl01_PageSizeComboBox_ClientState=&ctl01_TemplateBody_WebPartManager1_gwpciNewQueryMenuCommon_ciNewQueryMenuCommon_ResultsGrid_Grid1_ClientState=&ctl01%24TemplateBody%24ContentPage1%24HiddenDownloadPathField=&ctl01_ciSecondary_SubNavControl_SubNavigationTree_ClientState=%7B%22expandedNodes%22%3A%5B%5D%2C%22collapsedNodes%22%3A%5B%5D%2C%22logEntries%22%3A%5B%5D%2C%22selectedNodes%22%3A%5B%5D%2C%22checkedNodes%22%3A%5B%5D%2C%22scrollPosition%22%3A0%7D&ctl01%24ciSideContent%24ContentRecordTemplateArea%24AlertDisplay%24NoAlertMessageHiddenField=&ctl01%24TemplateScripts%24timeoutsoonmsg=PGgyPllvdSBhcmUgYWJvdXQgdG8gYmUgc2lnbmVkIG91dDwvaDI%2BDQo8cD5Zb3Ugd2lsbCBiZSBzaWduZWQgb3V0IGluIDxzdHJvbmc%2BW1NlY29uZHNSZW1haW5pbmddPC9zdHJvbmc%2BIHNlY29uZHMgZHVlIHRvIGluYWN0aXZpdHkuIFlvdXIgY2hhbmdlcyB3aWxsIG5vdCBiZSBzYXZlZC4gVG8gY29udGludWUgd29ya2luZyBvbiB0aGUgd2Vic2l0ZSwgY2xpY2sgIlN0YXkgU2lnbmVkIEluIiBiZWxvdy48L3A%2B&ctl01%24TemplateScripts%24timeoutsoonstaysignintxt=U3RheSBTaWduZWQgSW4%3D&ctl01%24TemplateScripts%24timeoutsoonlogouttxt=U2lnbiBPdXQ%3D&ctl01%24TemplateScripts%24stayLoggedInURL=&ctl01%24TemplateScripts%24logoutUrl=aHR0cHM6Ly9hbG0uaW1pc2Nsb3VkLmNvbS9BTEFMTS9hc2ljb21tb24vY29udHJvbHMvc2hhcmVkL2Zvcm1zYXV0aGVudGljYXRpb24vbG9naW4uYXNweD9TZXNzaW9uVGltZW91dD0xJlJldHVyblVybD0lMmZBTEFMTSUyZkFMQUxNJTJmQWJvdXQlMmZBTE0tTXVuaWNpcGFsLURpcmVjdG9yeS5hc3B4JTNm&ctl01_GenericWindow_ClientState=&ctl01_ObjectBrowser_ClientState=&ctl01_ObjectBrowserDialog_ClientState=&ctl01_WindowManager1_ClientState=&__EVENTTARGET=ctl01%24TemplateBody%24WebPartManager1%24gwpciNewQueryMenuCommon%24ciNewQueryMenuCommon%24ResultsGrid%24Grid1%24ctl00%24ctl03%24ctl01%24ctl{no}&__EVENTARGUMENT=&__VIEWSTATE={viewstate}&__VIEWSTATEGENERATOR=F8BB5AFA&PageInstanceKey={q[3]}&__RequestVerificationToken={token}&TemplateUserMessagesID=ctl01_TemplateUserMessages_ctl00_Messages&PageIsDirty=false&IsControlPostBack=1&__ASYNCPOST=true&"
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8,hi;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'ASP.NET_SessionId=pe0kt4kduxxu5hd3arfyonp0; __RequestVerificationToken=hemRMm5w0tjsbRUI1Gx6VNIKs4INQr7ScObH9vFZVCQOfQR2tEUw0rNAsUXnoBbLLVS88b2wLJmsl0ugyA1sMhT9_zYSLN8SWFNglW8DDQ41; __RequestVerificationToken=hemRMm5w0tjsbRUI1Gx6VNIKs4INQr7ScObH9vFZVCQOfQR2tEUw0rNAsUXnoBbLLVS88b2wLJmsl0ugyA1sMhT9_zYSLN8SWFNglW8DDQ41',
    'origin': 'https://alm.imiscloud.com',
    'priority': 'u=1, i',
    'referer': 'https://alm.imiscloud.com/ALALM/ALALM/About/ALM-Municipal-Directory.aspx',
    'request-id': '|bd63ef3131aeff932a0ecd690452dc0a.1ee31a93c1f445aa',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-bd63ef3131aeff932a0ecd690452dc0a-1ee31a93c1f445aa-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-microsoftajax': 'Delta=true',
    'x-requested-with': 'XMLHttpRequest'
    }
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.status_code)


    
    
def parsing(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    base = etree.HTML(str(soup))
    # sitestate = response.text.split('__VIEWSTATE|')[1].split('=|8|hiddenField|__VIEWSTATEGENERATOR')[0]
    sitestate = base.xpath('//input[@id="__VIEWSTATE"]/@value')[0].replace('=', "")
    token = base.xpath('//input[@id="__RequestVerificationToken"]/@value')[0]
    website_key = response.text.split('var gWebsiteKey = \'')[1].split('\';')[0]
    row = base.xpath('//table[@class="rgMasterTable CaptionTextInvisible"]/tbody/tr')
    ins_key = base.xpath('//input[@id="PageInstanceKey"]/@value')[0]
    # for i in row:
    #     name = i.xpath('td/text() | td/a/text() | td/a/@title')
    #     email = i.xpath('td[5]/a/@title')
    #     print(name)
    #     print(email)
        
    return sitestate,token,website_key,ins_key
    
     
     
        
def main():
    no = int('07')
    res = first_req()
    q = parsing(res)
    second_requesting(q,'07')
    
        
    
    
if __name__ == "__main__":
    main()


