![image](https://travis-ci.org/soumendrak/stock_price_change_alert.svg?branch=master)
# stock_price_change_alert
Send SMS if any of the predefined share price fluctuates above a certain customizable level.
## Usage
`git clone https://github.com/soumendrak/stock_price_change_alert.git`
### Changing user specific values
Change the following values in `customizable_data.py` file.
- `numbers`:   Mention a list of number(s) to which you want to send SMS.
- `username`:  Username of your Way2SMS account.
Most probably the username will be your registered mobile number.
- `password`:  Password for your Way2SMS account.
- `username` and `password` can be obtained by registering at http://site23.way2sms.com/content/index.html
- `watchlist`: You can update this with the shares for which you want to monitor.
- `defined_limit`: This is the threshold limit in percetages. If the share price increased or decreased
above the mentioned limit, it will trigger for SMS.
### Running the program
`python stock_alert.py`
### Output
> Checking quotes for EICHERMOT  
> EICHERMOT:0.58  
> Checking quotes for INDIGO  
> INDIGO:-4.12  
> sending SMS for INDIGO  
> sending `INDIGO price has DOWN by 4.12 percent. to ['XXXXXXXXXX']`  
> success  
> SMS for INDIGO sent successfully  
> Checking quotes for SBIN  
> SBIN:-0.84  


You will receive `INDIGO price has DOWN by 4.12 percent.` in your mentioned number.
