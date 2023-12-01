import segno

micro_qrcode = segno.make('Rain', error='q')
micro_qrcode.save('rain.png', dark='darkblue', data_dark='steelblue', scale=5)