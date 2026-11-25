# ការរៀបចំ (Setup)

អ្នកត្រូវការតែ web browser មួយ និងគណនី Google មួយប៉ុណ្ណោះ។ notebook នីមួយៗមានច្បាប់ចម្លងនៃប្រព័ន្ធវគ្គសិក្សានៅក្នុងខ្លួនវា។ ដូច្នេះ **មិនចាំបាច់ install អ្វីទាំងអស់ ហើយមិនចាំបាច់ upload file ណាមួយទេ**។

សូមអានទំព័រនេះ មុនពេលអ្នកបើក notebook ដំបូងរបស់អ្នក។ សូមត្រឡប់មកទំព័រនេះវិញ នៅពេល notebook មិនដំណើរការ។ និស្សិតភាគច្រើនប្រើជម្រើស A។ ជម្រើស B មានសម្រាប់អ្នកដែលចូលចិត្តធ្វើការដោយគ្មាន internet (offline)។

## ជម្រើស A · Google Colab (ណែនាំ)

1. នៅ [ទំព័រដើមរបស់វគ្គសិក្សា](README.md) ចុច **Open in Colab** សម្រាប់សប្ដាហ៍របស់អ្នក។
2. **File → Save a copy in Drive**។ ចូរធ្វើបែបនេះមុនគេ រៀងរាល់សប្ដាហ៍។ ការកែប្រែដែលអ្នកធ្វើ មុនពេល save ច្បាប់ចម្លង អាចបាត់បង់បាន។
3. ធ្វើការក្នុងច្បាប់ចម្លងរបស់អ្នក (ឈ្មោះរបស់វាចាប់ផ្ដើមដោយ "Copy of")។
4. ចូរ Run setup cell ទីមួយ៖ **▶ សូម run cell នេះមុនគេ (setup)**។ វា print `✅ ប្រព័ន្ធ FoodBridge រួចរាល់ហើយ`។
5. ធ្វើការពីលើចុះក្រោម។ ចុច **Shift + Enter** ដើម្បី Run cell មួយ។

**អ្វីដែលគួរដឹងអំពី Colab**

- ប្រសិនបើ Colab ប្រាប់ថា runtime ត្រូវបាន reset ឬដាច់ការតភ្ជាប់ (disconnected) សូម Run setup cell ម្ដងទៀត។ បន្ទាប់មក សូម Run cell ដែលអ្នកត្រូវការ។
- នៅពេលអ្នកច្រឡំ សូមប្រើ **Runtime → Restart session and run all**។ វា Run អ្វីៗទាំងអស់ឡើងវិញពីដំបូង តាមលំដាប់។
- **ចាប់ពីសប្ដាហ៍ទី 4 តទៅ** setup cell នឹងសួរដើម្បីភ្ជាប់ Google Drive ដើម្បីរក្សាទុក folder `my_foodbridge/` របស់អ្នកនៅក្នុង `MyDrive/my_foodbridge` ហើយនៅជាមួយអ្នកពីសប្ដាហ៍មួយទៅសប្ដាហ៍មួយ។ ប្រសិនបើអ្នកមិនអនុញ្ញាតឱ្យភ្ជាប់ Drive ទេ Colab នឹងរក្សា `my_foodbridge/` ក្នុង folder បណ្ដោះអាសន្នសម្រាប់វគ្គនោះប៉ុណ្ណោះ — វា **បាត់ទៅវិញនៅពេល runtime ដាច់ការតភ្ជាប់** (សូមទាញយកច្បាប់ចម្លង ឬភ្ជាប់ Drive វិញ ប្រសិនបើអ្នកចង់រក្សាទុក file របស់អ្នក)។ ចំណែក notebook របស់អ្នកផ្ទាល់ នៅមានសុវត្ថិភាពក្នុង Drive ជានិច្ច នៅពេលអ្នក save ច្បាប់ចម្លង។
- បច្ចុប្បន្ន Colab ប្រើ Python 3.13 (បានពិនិត្យនៅខែវិច្ឆិកា ឆ្នាំ 2026)។ វគ្គសិក្សានេះដំណើរការជាមួយ Python ណាក៏បាន ចាប់ពី 3.9 ឡើងទៅ។ ដូច្នេះ Colab កំណែថ្មីជាងនេះ ក៏មិនអីដែរ។

## ជម្រើស B · កុំព្យូទ័រផ្ទាល់ខ្លួនរបស់អ្នក

ប្រសិនបើ Colab មិនមែនជាជម្រើសសម្រាប់អ្នកទេ notebook ដដែលនេះ ក៏ដំណើរការនៅលើកុំព្យូទ័រផ្ទាល់ខ្លួនរបស់អ្នកបានដែរ។ សូមប្រើជម្រើសនេះ ប្រសិនបើអ្នកចូលចិត្តធ្វើការដោយគ្មាន internet (offline)។

1. Install **Python 3** កំណែចុងក្រោយពី [python.org](https://www.python.org/downloads/) (កំណែណាក៏បាន ចាប់ពី 3.9 ឡើងទៅ ក៏ប្រើបានដែរ)។
2. Install Jupyter និង matplotlib៖ បើក terminal ហើយ Run `python -m pip install notebook matplotlib` (នៅលើកុំព្យូទ័រខ្លះ ត្រូវប្រើ `python3 -m pip install notebook matplotlib`)។ `matplotlib` ត្រូវបានប្រើសម្រាប់គូរក្រាហ្វ (chart) ក្នុងសប្ដាហ៍ទី 8–9។
3. នៅទំព័រដើមរបស់វគ្គសិក្សា សូមប្រើ **Download** ដើម្បីរក្សាទុក file `.ipynb` របស់សប្ដាហ៍នោះ ក្នុង folder មួយ។
4. ក្នុង terminal នៅ folder នោះ សូម Run `python -m notebook` ហើយបើក file នោះ។
5. ចូរ Run setup cell។ វាបង្កើត folder `foodbridge_kit` (ហើយចាប់ពីសប្ដាហ៍ទី 4 តទៅ ក៏បង្កើត folder `my_foodbridge` របស់អ្នកដែរ) នៅជាប់នឹង notebook។

VS Code ជាមួយ extension Python និង Jupyter ក៏ប្រើបានដែរ៖ បើក file `.ipynb` ហើយជ្រើសរើស kernel Python 3។

## Final project នៅផ្ទះ (ស្រេចចិត្ត)

Final project របស់អ្នក គឺជា folder `my_foodbridge/` ផ្ទាល់ខ្លួនរបស់អ្នក។ ដើម្បី run វានៅក្រៅ notebook៖

1. ទាញយក (download) folder នោះ (Google Drive → ចុចកណ្ដុរស្ដាំលើ `my_foodbridge` → **Download**) ហើយពន្លា (unzip) វា។
2. បើក terminal នៅក្នុង folder `my_foodbridge/`។
3. Run `python app.py` (ប្រើ `python3` នៅលើ Mac ឬ Linux) រួចវាយ `1`, `2`, `3` ឬ `q`។

Web app (`bridge.start_web`) ដំណើរការតែក្នុង notebook ប៉ុណ្ណោះ។

[FoodBridge kit ZIP](/downloads/foodbridge_kit.zip) គឺជាប្រព័ន្ធដដែល ជាមួយ default settings។

## ពេលមានបញ្ហា

បញ្ហាភាគច្រើន មានវិធីដោះស្រាយរហ័ស។ ចូររកអ្វីដែលអ្នកឃើញ នៅក្នុងតារាង ហើយធ្វើតាមអ្វីដែលតារាងប្រាប់។

| អ្វីដែលអ្នកឃើញ | អ្វីដែលត្រូវធ្វើ |
|---|---|
| `NameError: name 'bridge' is not defined` | ចូរ Run setup cell មុនសិន។ |
| ឈ្មោះមួយដែលអ្នកបានបង្កើត លោតសារថា "not defined" | ចូរ Run cell ដែលកំណត់ឈ្មោះនោះ ឬប្រើ **Restart session and run all**។ |
| ការពិនិត្យមួយបង្ហាញ ❌ | សូមអានការណែនាំ 💡 នៅខាងក្រោមវា។ ការពិនិត្យមិនដែលបញ្ឈប់ notebook របស់អ្នកទេ៖ សូមកែ ហើយ Run ម្ដងទៀត។ |
| `⚠️ … របស់អ្នកមិនដំណើរការ ប្រព័ន្ធបានប្រើ default` | function របស់អ្នកបាន crash ឬបាន return អ្វីមួយដែលមិនបានរំពឹងទុក។ ដូច្នេះ ប្រព័ន្ធបានប្រើវិធានរបស់ខ្លួនវាជំនួស។ សូមអានសារនោះ។ |
| `bridge.show()` សម្គាល់ file មួយដោយ `🔧` (កំណែគំរូ) | file នោះមិនទាន់មានក្នុង `my_foodbridge/` ឬវាមានកំហុស Python។ សូមអានកំណត់ចំណាំបញ្ហាក្នុង `bridge.show()` ហើយ Run cell `%%writefile` ម្ដងទៀត ឬកែ file នោះ។ |
| setup cell បង្ហាញលេខ version ថ្មី | មិនអីទេ៖ notebook បានពន្លា (unpack) ឯកសារវគ្គសិក្សាកំណែថ្មី។ folder `my_foodbridge/` របស់អ្នក (និង `my_settings.py` / `my_rules.py` ពីមុន) នៅដដែល។ |

នៅតែមិនទាន់ដោះស្រាយបាន? សូមមើល [សំណួរ និងជំនួយ (English)](../CONTRIBUTING.md)។
