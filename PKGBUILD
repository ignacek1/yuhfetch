pkgname=yuhfetch
pkgver=2.2
pkgrel=1
pkgdesc="A tool for fetching and displaying system information in a colorful way."
arch=('any')
url="https://github.com/ignxcy/yuhfetch"

depends=('git' 'python3')

package() {
  cd "$srcdir"
  git clone "$url" "$pkgname-$pkgver"
  cd "$pkgname-$pkgver"
  sudo make install
}
