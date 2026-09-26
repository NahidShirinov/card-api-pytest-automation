# Card API Tests

`http://localhost:8090` uzerinde isleyen Card Status API ucun pytest testleri.

## Qurasdirma
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Islətmek
```
pytest                    # hamisi
pytest -m smoke           # yalniz smoke testler
pytest -m negative        # yalniz negativ testler
pytest --html=report.html # HTML hesabat
```

## Struktur
| Qovluq | Ne ucun |
|---|---|
| `config/` | .env-den ayarlari oxuyur |
| `clients/` | API sorgulari (her endpoint bir metod) |
| `models/` | Cavablarin strukturu (pydantic) |
| `data/` | Test melumati yaradan funksiyalar |
| `tests/` | Testlerin ozu |

## Tapilan buglar
- Bos body (`{}`) 400 yox, 500 qaytarir
- Movcud olmayan status (`XYZ`) qebul olunur
