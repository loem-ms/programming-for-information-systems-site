# ការរៀបចំ (Setup)

អ្នកត្រូវការតែ web browser មួយ និងគណនី Google មួយប៉ុណ្ណោះ។ notebook នីមួយៗមានច្បាប់ចម្លងនៃប្រព័ន្ធរបស់វគ្គសិក្សានៅក្នុងខ្លួនវា ដូច្នេះ **មិនចាំបាច់ install អ្វី ហើយក៏មិនចាំបាច់ upload file ណាដែរ**។

## ជម្រើស A · Google Colab (ណែនាំ)

1. នៅ [ទំព័រដើមរបស់វគ្គសិក្សា](README.md) ចុច **Open in Colab** សម្រាប់សប្ដាហ៍របស់អ្នក។
2. **File → Save a copy in Drive។** ធ្វើបែបនេះមុនគេ រៀងរាល់សប្ដាហ៍។ ការកែប្រែដែលអ្នកធ្វើ មុននឹង save ច្បាប់ចម្លង អាចបាត់បង់។
3. ធ្វើការក្នុងច្បាប់ចម្លងរបស់អ្នក (ឈ្មោះរបស់វាចាប់ផ្ដើមដោយ "Copy of")។
4. Run code cell ទីមួយ **▶ សូម run cell នេះមុនគេ (setup)**។ វា print `✅ ប្រព័ន្ធ Food Rescue រួចរាល់ហើយ`។
5. ធ្វើពីលើចុះក្រោម។ ចុច **Shift + Enter** ដើម្បី run cell មួយ។

**អ្វីដែលគួរដឹងអំពី Colab**

- បើ Colab ប្រាប់ថា runtime ត្រូវបាន reset ឬដាច់ការតភ្ជាប់ (disconnected) សូម run setup cell ម្ដងទៀត បន្ទាប់មក run cell ដែលអ្នកត្រូវការ។
- ពេលអ្នកច្រឡំ សូមប្រើ **Runtime → Restart session and run all**។ វា run អ្វីៗទាំងអស់ឡើងវិញពីដំបូង តាមលំដាប់។
- File ដែល code របស់អ្នកសរសេរ (ឧទាហរណ៍ `my_offers.json` ក្នុងសប្ដាហ៍ទី 7) នៅក្នុង folder បណ្ដោះអាសន្ន ហើយ **បាត់ទៅវិញពេល runtime reset**។ ចំណែក notebook របស់អ្នកផ្ទាល់ នៅមានសុវត្ថិភាពក្នុង Drive។
- បច្ចុប្បន្ន Colab ប្រើ Python 3.13 (បានពិនិត្យនៅខែវិច្ឆិកា ឆ្នាំ 2026)។ វគ្គសិក្សានេះដំណើរការជាមួយ Python ណាក៏បាន ចាប់ពី 3.9 ឡើងទៅ ដូច្នេះ Colab កំណែថ្មីជាងនេះក៏មិនអីដែរ។

## ជម្រើស B · កុំព្យូទ័រផ្ទាល់ខ្លួនរបស់អ្នក

ប្រើជម្រើសនេះ បើអ្នកចូលចិត្តធ្វើការដោយគ្មាន internet (offline)។

1. Install **Python 3** កំណែចុងក្រោយពី [python.org](https://www.python.org/downloads/) (កំណែណាក៏បាន ចាប់ពី 3.9 ឡើងទៅ)។
2. Install Jupyter: បើក terminal ហើយ run `python -m pip install notebook` (នៅលើកុំព្យូទ័រខ្លះ `python3 -m pip install notebook`)។
3. នៅទំព័រដើមរបស់វគ្គសិក្សា ប្រើ **ទាញយក** (Download) ដើម្បីរក្សាទុក file `.ipynb` របស់សប្ដាហ៍នោះក្នុង folder មួយ។
4. ក្នុង terminal នៅ folder នោះ run `python -m notebook` ហើយបើក file នោះ។
5. Run setup cell។ វាបង្កើត folder `food_rescue_kit` នៅជាប់នឹង notebook។

VS Code ជាមួយ extension Python និង Jupyter ក៏ប្រើបានដែរ: បើក file `.ipynb` ហើយជ្រើសរើស kernel Python 3។

## Final project នៅផ្ទះ (ស្រេចចិត្ត)

ក្នុង final project (កម្រិតទី 4) អ្នកអាចទាញយកប្រព័ន្ធ **ផ្ទាល់ខ្លួនរបស់អ្នក** ជា ZIP ហើយ run វានៅក្រៅ notebook:

1. ពន្លា (unzip) `my_food_rescue.zip`។
2. បើក terminal នៅក្នុង folder `food_rescue_kit`។
3. Run `python run_web.py` ហើយបើក http://localhost:8000 ក្នុង browser របស់អ្នក។ បញ្ឈប់វាដោយចុច **Ctrl + C**។
4. `python run_menu.py` បើក menu ជាអក្សរ (text menu)។ `python run_tests.py` run test របស់ប្រព័ន្ធ។

[Food Rescue kit ZIP](/downloads/food_rescue_kit.zip) គឺជាប្រព័ន្ធដដែល ជាមួយ default settings។ ដើម្បីឃើញអេក្រង់ជាភាសាខ្មែរ សូមដាក់ `LANGUAGE = "km"` ក្នុង `my_settings.py` (ZIP ផ្ទាល់ខ្លួនរបស់អ្នក ដែលអ្នកទាញយកពី notebook មានបន្ទាត់នេះរួចហើយ)។

## ពេលមានបញ្ហា

| អ្វីដែលអ្នកឃើញ | អ្វីដែលត្រូវធ្វើ |
|---|---|
| `NameError: name 'fr' is not defined` | Run setup cell មុនសិន។ |
| ឈ្មោះមួយដែលអ្នកបានកំណត់ ត្រូវបានប្រាប់ថា "not defined" | Run cell ដែលកំណត់ឈ្មោះនោះ ឬប្រើ **Restart session and run all**។ |
| ការពិនិត្យមួយបង្ហាញ ❌ | អានការណែនាំ 💡 នៅខាងក្រោមវា។ ការពិនិត្យមិនដែលបញ្ឈប់ notebook របស់អ្នកទេ: កែ ហើយ run ម្ដងទៀត។ |
| `⚠️ … របស់អ្នកមិនដំណើរការ ប្រព័ន្ធបានប្រើ default` | function របស់អ្នកបាន crash ឬបាន return អ្វីមួយដែលមិនរំពឹងទុក ដូច្នេះប្រព័ន្ធបានប្រើវិធានរបស់ខ្លួនវាជំនួស។ សូមអានសារនោះ។ |
| setup cell បង្ហាញលេខ version ថ្មី | មិនអីទេ: វគ្គសិក្សាកំណែថ្មីជាងមួយត្រូវបានដកយក (unpack)។ `my_settings.py` និង `my_rules.py` របស់អ្នកនៅដដែល។ |

នៅតែមិនទាន់ដោះស្រាយបាន? សូមមើល [សំណួរ និងជំនួយ (English)](../CONTRIBUTING.md)។
