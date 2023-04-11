import os
import win32com.client as win32

def send_email(to, subject, body, attachments=None):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    
    if attachments:
        for attachment in attachments:
            mail.Attachments.Add(attachment)
    
    mail.Send()

# Example usage: send an email with attachment
to = 'cao.loc.huynh@ericsson.com'
subject = 'Test email with attachment'
body = 'This is a test email with an attachment.'
attachments = [r'C:\Coding\Python\Codes\File\H01033__LN.log']

send_email(to, subject, body, attachments)