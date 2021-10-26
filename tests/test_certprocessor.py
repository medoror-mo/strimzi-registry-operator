"""Tests for the certprocessor module.
"""

import pytest

from strimziregistryoperator.certprocessor import (
    create_truststore, create_keystore)


@pytest.fixture
def cluster_ca_cert():
    return """
-----BEGIN CERTIFICATE-----
MIIFLTCCAxWgAwIBAgIUYThZW2C1f6pLM6JbgsuQusZDpKUwDQYJKoZIhvcNAQEN
BQAwLTETMBEGA1UECgwKaW8uc3RyaW16aTEWMBQGA1UEAwwNY2x1c3Rlci1jYSB2
MDAeFw0yMTEwMTkyMDQ4NDFaFw0yMjEwMTkyMDQ4NDFaMC0xEzARBgNVBAoMCmlv
LnN0cmltemkxFjAUBgNVBAMMDWNsdXN0ZXItY2EgdjAwggIiMA0GCSqGSIb3DQEB
AQUAA4ICDwAwggIKAoICAQDPEjmS0/K6o+o9zLwYNo7WMeHLCsHnbw8aljDBUXKR
duftlQlIUQGJC22AH/kmxaHarIAZGhvZtSSpBM662oI9DGL/5Vt7ASvlzch2U5Rx
NHk3R8+Whsnc6UzZsKxvpronoG638UXi7g8nbCIJUUzTjwp/71T1jugfG6cbZPfs
Mj955pM3RNT8JNlLSU5LUj/DEU+HZfsAVYULUl70CYhHFo9yVA4cag2/wBXr5ejQ
oVi5TpFFcnA6Qi0kcECbdX7Tt99MBXcMd2Hc8Rw/nZZYF5oiRYGp0mlMqS/ev1zJ
OTN5Wg8qxPKaz3XocaEMwT+3hLehNEVy8KMsr2fsgiREUYrXjMppnkBLELq6p6uM
kmzvJ8IPbOUA/crnfVGWGNtsOVUCGVOdJA0KHEIlqiZbk5LWWBGwniBEs7rHA/Pm
6eCFmwhkyX/A3IvluxWksyTKlUg/RLLY88H3RWEnf+PMScFO58wnA0jfZ9+e5fRw
b9ozOk+V5vc9AZB0PdJzC0wRzJN3pERC77zrJrGOGFRvgz6Bg86LoWhzH3D2TGpF
49eNJS9NPgdOC7u2y7WvgkR2Q1TvHndDrm+ZPw+gcBuJB234d+zBY8KQSKOE4qo1
zveJCuaaTe9yT/bTEcrL4gipbJ3i2t9tCUkED8AJepXAzT9jXcesGH9KQ9v4f0Sk
awIDAQABo0UwQzAdBgNVHQ4EFgQU1wq9E8qWO93Ln1brxd0/AxmsPt0wEgYDVR0T
AQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAQYwDQYJKoZIhvcNAQENBQADggIB
AM5/4tYT4X9f29HlYhBNooH394cKUfrodObFHYIywh20Mah7iyw2Os12OxyzKNVp
YjTTgPFHl0KmExOUglJvSorY2TVfiUiq7QzT5XwRnosmSryqMR8B/vMyiQEn1of+
vEID4k+eB8bdFlQCV6xmyR3swcwM0aOpne29D6x5p/ilOknXNA2xlxUzF470Awvm
NbLHW1ODtyDlvHS3eS6ofN3Sf2nR4r8i8fF/NceL+VDnVOl0sLAj+awgNBeEuUQl
zLCmcgqmugFT2haxOmr9IDlXNXSI8YFqEfE2nHgLo17lq1/rDThi78PXlgZpprT4
1hpEocD/t+6nJePQVzzV1CyTihcCRwVYbSI+T4Z2c+FYvc5vdiQJ5hoS7QcI1ns4
vbgyxXpw4Wz+/3IAga6qjsYUb6DN70JmLy3pwB2aVDN8lvmxlOvhtkJcDBkgFCLc
9LGEh/CHonDIYG6st43Te+fzJk2B8IO8nllOZMh1aAX0/9yNXco/2E7R6DKuhnj4
8YxwugJcZ7iydK+giatSlF059AD5nqk0wp4CQxw6nhQcJsGxMHfmSl6tlZwhUJrV
SnJ2auomP4fc6elwr9LCBOl1HpBZ5XkijO7WLL1zCGBDYIu45Ruy16BYN1EWqnjJ
sr7xIs5yJ9mzWcjYQ/9XJkIh5j0whhVFB17W9bzEnTjs
-----END CERTIFICATE-----
    """


@pytest.fixture
def user_ca_cert():
    return """
-----BEGIN CERTIFICATE-----
MIIFLTCCAxWgAwIBAgIUbo4/n9VcsiNCd8oFE3eNxT9LMF8wDQYJKoZIhvcNAQEN
BQAwLTETMBEGA1UECgwKaW8uc3RyaW16aTEWMBQGA1UEAwwNY2xpZW50cy1jYSB2
MDAeFw0yMTEwMTkyMDQ4NDFaFw0yMjEwMTkyMDQ4NDFaMC0xEzARBgNVBAoMCmlv
LnN0cmltemkxFjAUBgNVBAMMDWNsaWVudHMtY2EgdjAwggIiMA0GCSqGSIb3DQEB
AQUAA4ICDwAwggIKAoICAQD2ePC5XQc5EqWSMpFw4sJh4txNRTiJGETrkxRT6ABE
bd+LqLOqXvOHXt1Dcl87ccbdVHwTTTZMXgvtVh7EEl1UQdh0OKgkQREpdnBU5dXz
jshZFPBhEHTaZ9uxUZFE02iwHadR/IJ6bG3rG8JSJd1O726VqqhQ2D9dX4J304vj
vb1ogQHXOkyXJUQKcnYQmlfXZro4RkBE3cafpqvr+7DbMIapdvJSSKF+3td8KooF
wLJfpAU8H1WIIZEXdKPNxl6bAa6vIraxMcYoj6doTuSLaT4tvEXa+l9TCbFVszNY
qNbf8youIZB5AF9/pR+Ozmpsgu/9ywJ+L6RN53jm1GnLAmXBTiWzsEg8S0f/fW/6
VY5DMQHdluTLnSoMC7PnLw8QA89M9/7V/6EVJ/vdrxPZBdXD1DHCPvuraaRx5sj6
QwRwjwuWai0cvIKUHaS/RiT1pFsZW3xPDPWNUHDHfDQX0uXnSkAOr1X7s7yf1vOf
by705rcHGTGZ+hPqBDF6FyzR4gfx+hqAI4wEfmWkhh0pHlXXwdho5uuOVDSXwvh3
Kz6AXkUa1Hg6qzdOeKtTj8Yi4M8rYw3i3QwKQg2l6Jv4djywmMdpby+I0k0lFxjX
Qwb5dpsQyuvAAesn1l+I2I0MEB012ZefBouK4POufNPsxnBfMuCRRlXSPs4mhnZY
pQIDAQABo0UwQzAdBgNVHQ4EFgQU3wy3kXwVBL+2sDGb0erY317iw0swEgYDVR0T
AQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAQYwDQYJKoZIhvcNAQENBQADggIB
AN6I7LNWNbbwAmuP6tZ1gM1ykvdDgcdTqVwTe2h34BSXRhmNwJYgTCfnw38xBfY5
kSjaI7Wsr8UWatiaJbzfM6q6h588ueWZaTWqH2FOoemULX4eboLPJZFA4VO9MdHY
jF2s5GSN3bculUYOVAXLvf/yMZ+CqLmKAEgR8+Lu0AP8WHNAXVgdD5QIPYod4D78
tQzQjNki7tHTta+dlLF98MWpdAGUmYVZA/od309tpHf/p76880aPdxzPTpX0sBU1
B2TDkmaZATRNgehlPV/Bkh4qhHZHrPtFOnOH0+pKV4TV+20zj1wKvt8Vjz8F7pV9
o5RwLtheF6tS5gf0kJAVGN/80lPtNtzJePw7ecF7ZicEiiEdY3wgubjh6znsXazk
OO3a2fhvJkaAGuis6fb+ApWM6xvtpGL+o//ZjP/nYVfueChTvHnsEB87JvgETZU0
LBtbcfMZcirwbbo7RCiXkzouf2bIbHEU2IHFC0EUHide++YEto2RUZIwPfHNtgsi
lyugVAaMUJ//1VHGIbW+9HkmkQ+2ibc6zi0ec/slwgJEGPCQlODKV3f6/Q9ldfCB
Nx27hmW1s71b3do1YX7MYFB29XqoKS7jgMw5935ic4d/QHuGDWGa1RIsSj56nVeQ
16Hw6YY91i4Jw3RPeEVAY+NPuJLIK1+PvyUy4G0lVtjn
-----END CERTIFICATE-----
"""


@pytest.fixture
def user_cert():
    return """
-----BEGIN CERTIFICATE-----
MIIEHjCCAgagAwIBAgIUVGG6iqjc2FBaI0fOQ3D8bxwQZ3owDQYJKoZIhvcNAQEN
BQAwLTETMBEGA1UECgwKaW8uc3RyaW16aTEWMBQGA1UEAwwNY2xpZW50cy1jYSB2
MDAeFw0yMTEwMjAxNjI5NTJaFw0yMjEwMjAxNjI5NTJaMCQxIjAgBgNVBAMMGWNv
bmZsdWVudC1zY2hlbWEtcmVnaXN0cnkwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
ggEKAoIBAQDxKUrgzIKjUPjCvNegmf9uwna+lnXuZgcegWlwsAlkGtWFTM1E4d2c
KdMnj3omqfC6zkstZatGFthAOfRy5Q+LVeOgIkIS9sy8Iuwqip03RFt6gXyOdmJy
YJyyXnNdwf6jU7za1/th/b4VU06jSciU/ebx1S0KR7rWJgpqKnufJIXotSaoYs6U
1NH4kqHfRpGiPshDBjBglUxJ8R1RxTlDC9G/kGNO0B0RXy1XsHmK4qpJkRZ8Y2ma
WUSRgUDNaHDs5EGF9PgtA7xlhMAOK/7EMr0WV+rsFcQ87M8k7oye+bOQLZA4u9lr
kWdgfhoL9oxEnGn/CXg3EO0u/mX2RNnfAgMBAAGjPzA9MB0GA1UdDgQWBBTqfJLU
zbfrgK50i+Zw7mGsXPzZ3DAMBgNVHRMBAf8EAjAAMA4GA1UdDwEB/wQEAwIFoDAN
BgkqhkiG9w0BAQ0FAAOCAgEA76dCO9dbPz8QNcmegvBYZ0PCXqZ4iKDeL5uQxn/u
08EstDnoNIGmqJLM6Jana+LelJdSLhtD1ioOWtDNqvPXMxXKKqHx3ugyjkVdqA8z
qy3x89vdEej5elY8nE5/8PaYfz5SWZcmDqYVjnCqz54uoZVN5p3VCzTuPAGUVJfn
PlIsA5/3ticFLIHACu4ZDVZLmQbGlGQhfjtNIC4pb1AJKWGLfPVmMSqCjPP3ZsOQ
Oe4BE5gSy+nOL0xmaxOiZVRIhcjCib0nF6ZvTj8SvpYi+3N2shWMjLBjvfnJQHsr
aHqBbnQ7N8vMTCc2prSygU0TN8XNdcOfzOVPXaJz3E/f8mm1eaYERGUiRiykAeFT
gKcN5RSM0QvabDodnLUqJ7SftWDiBOEo66P8CBMb96tdllyhPHIycmfkPSrl1BBJ
qCgv6P/ZVraI397VPIlDu1I7xz8U4JU8AUPuUgxUW5+kgasG4bZgPLvWZ6pusedh
zNgL8uCPlvaU7vaRdc1qpF//XNiaqm4UaCPJWSgySH1iVYvTYVih3DB0GjnjFnSs
zOUyqorkB4musyrUObqmOsts6Agi05WQaBWXmySUxzKP4KSqAECdYJ/Q8C9cOQVG
FpRNTBFdldfAuhFijPqvNG383TbjFGoJl/aaFn6oZTq7QJ8dJ4GfHasahNXUObng
xng=
-----END CERTIFICATE-----
"""


@pytest.fixture
def user_key():
    return """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDxKUrgzIKjUPjC
vNegmf9uwna+lnXuZgcegWlwsAlkGtWFTM1E4d2cKdMnj3omqfC6zkstZatGFthA
OfRy5Q+LVeOgIkIS9sy8Iuwqip03RFt6gXyOdmJyYJyyXnNdwf6jU7za1/th/b4V
U06jSciU/ebx1S0KR7rWJgpqKnufJIXotSaoYs6U1NH4kqHfRpGiPshDBjBglUxJ
8R1RxTlDC9G/kGNO0B0RXy1XsHmK4qpJkRZ8Y2maWUSRgUDNaHDs5EGF9PgtA7xl
hMAOK/7EMr0WV+rsFcQ87M8k7oye+bOQLZA4u9lrkWdgfhoL9oxEnGn/CXg3EO0u
/mX2RNnfAgMBAAECggEBAKn+loayAqCG8mOrZEAUbecwcy3Tt9vN1dTeGmpR3LzQ
4ZRuV//nSyTKosqvK8bXYhb8VifxE/N7JQLZF4RqDTQF3kfB/luJ1zYDVACE51/O
8sD/R8LQloLTsYFWbPI5TnrpCyYku1IO4I/9wl/+IcNM2x+7Sl2FxKEx/YNq4OuD
H/++W6hQbV9EOED/W5MwS/a8JG3u8BgUlSErnS4VXCGiwyIddqYs9Rb+cHWkgcVC
Dluo9OrJUtCqpaZiT6LtHdQWhfdGCgQb9t0aG9BSe1CSLI4hlcvHk/RSuBKsinaA
O9LecyOPtF1OCCzU4e96vmTYg8/Y1x8YI2eY6BIY3YkCgYEA/CVtt/u2rGGOhMIp
mHx344x8HHyQyq71pAZLCDMf2FmFR2Ld0/RT3bHTTf6jElv07EYULmLWp02QqLWQ
gomjtNUxUcHMJK9FMaBpTxnT32vuSIrFUz7odLOO49gORrkof1KJ3Bq8VwEzj6LX
pyJg1drf8KCFm4/4udB3LS6r7cMCgYEA9NjiIE8CfmxjLlK2ezXpM2KgM7lcrTCi
5HDL8g4L2FCK14n+7xzBYEjNGrPHGfsLclzjD4unOjIQyPBfQFxhLYJPRc3yGjSM
A9Qw9v69CO9K1p3hg8T5wRIy9CzyuyCrYbJvkyUxGcDfXHii3tBx4zZx2rbnWS/X
H83BU3vsVbUCgYBfydRJvc1i5VjgJGbq7/YXsun/ZG8ZIKhe3Kkqf0mMxk10liGR
gNNPeFu+2IqY0ehUzjaifJfxTO00um0guis/6nHnDkmAcjlGJht7mmM8EGOgmV9n
RZHHq+MPuaeKxJKW9AM9Y8bDAsjUu1dTviKte43xevnm5CXoaUKtHnrgQwKBgCOL
YLhj/+6ueW9+HnOgjewhwzP/Es8polwba+AF3f5XIvDLXbEEsaXyq6PWuW6yHSVL
CsN0+J/gKMOi8ZD8WDctFakCjsTzH+hmY31X2cV0R58EaHqim8dFhxQfelVkFr0m
FEB+Q7SDZWmdMbe69u2PN9QSfV9bLJW3XvtpoBOJAoGAS9T7ozd5OQudxHHfZmUd
XE5g/EGIFB8cTcKf/5kkqC9vj+ios53WtROTxyjUd1bbD1B75DegQ6K6DysC9zO1
35Hoe3SyDeKbjsdyM1mT0ueZhPrJBVCed/CuoMq5ZZGQrDgXNJ6t8O0eS4vuTkkT
AvMffvxA2Qccn47mmbmpqe4=
-----END PRIVATE KEY-----
"""


def test_create_truststore(cluster_ca_cert):
    # NB: This test depends upon the cert fixtures, which expire in 1 year
    # (2022-10-22).
    truststore, password = create_truststore(cluster_ca_cert,
                                             password='test1234')
    assert isinstance(truststore, bytes)
    assert len(truststore) > 0
    assert password == 'test1234'


def test_create_keystore(user_ca_cert, user_cert, user_key):
    # NB: This test depends upon the cert fixtures, which expire in 1 year
    # (2022-10-22).
    keystore, password = create_keystore(user_ca_cert, user_cert, user_key,
                                         password='test1234')
    assert isinstance(keystore, bytes)
    assert len(keystore) > 0
    assert password == 'test1234'
