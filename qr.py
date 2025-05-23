import click
import pyqrcode

defaultUrl = 'http://www.google.com/'

@click.command()
@click.argument('url')
@click.argument('output')
@click.option('--qrversion', default=6)
@click.option('--scale', default=5)
def main(url, output, qrversion:int=6, scale:int=5):
    code = pyqrcode.create(url, error='L', version=qrversion, mode='binary')
    code.png(output, scale=scale, module_color=[0, 0, 0, 0], background=[255, 255, 255])

if __name__ == '__main__':
    main()
