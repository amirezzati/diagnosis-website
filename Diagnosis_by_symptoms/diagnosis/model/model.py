import os
import pickle
import numpy as np
from keras.models import load_model

model_loc = 'diagnosis/model/model.hdf5'
classList_loc = 'diagnosis/model/output_classes.pkl'

# read output_classes using pickle
file_ = open(classList_loc, "rb")
output_classes = pickle.load(file_)
file_.close()

persion_disease = {
    '(vertigo) Paroymsal  Positional Vertigo': '(سرگیجه) سرگیجه موضعی پارویمسال',
    'AIDS': 'ایدز',
    'Acne': 'آکنه',
    'Alcoholic hepatitis': 'هپاتیت الکلی',
    'Allergy': 'آلرژی',
    'Arthritis': 'آرتروز',
    'Bronchial Asthma': 'آسم برونش',
    'Cervical spondylosis': 'اسپوندیلوز گردنی',
    'Chicken pox': 'آبله مرغان',
    'Chronic cholestasis': 'کلستاز مزمن',
    'Common Cold': 'سرماخوردگی',
    'Dengue': 'دنگی',
    'Diabetes ': 'دیابت',
    'Dimorphic hemmorhoids(piles)': 'هموروئید دو شکل (شمع)',
    'Drug Reaction': 'واکنش دارویی',
    'Fungal infection': 'عفونت قارچی',
    'GERD': 'ریفلاکس معده یا مری',
    'Gastroenteritis': 'گاستروانتریت (آنفلوانزای معده)',
    'Heart attack': 'حمله قلبی',
    'hepatitis A': 'هپاتیت A',
    'Hepatitis B': 'هپاتیت B',
    'Hepatitis C': 'هپاتیت C',
    'Hepatitis D': 'هپاتیت D',
    'Hepatitis E': 'هپاتیت E',
    'Hypertension ': 'فشار خون',
    'Hyperthyroidism': 'پرکاری تیروئید',
    'Hypoglycemia': 'هیپوگلیسمی',
    'Hypothyroidism': 'کم کاری تیروئید',
    'Impetigo': 'زرد زخم',
    'Jaundice': 'زردی',
    'Malaria': 'مالاریا',
    'Migraine': 'میگرن',
    'Osteoarthristis': 'آرتروز',
    'Paralysis (brain hemorrhage)': 'فلج (خونریزی مغزی)',
    'Peptic ulcer diseae': 'زخم پپتیک',
    'Pneumonia': 'ذات الریه',
    'Psoriasis': 'پسوریازیس',
    'Tuberculosis': 'سل',
    'Typhoid': 'حصبه',
    'Urinary tract infection': 'عفونت مجاری ادراری',
    'Varicose veins': 'رگ های واریسی'
}


def predict(features):
    model = load_model(model_loc)
    result = model.predict(np.array([features]), verbose=0)
    class_num = np.argmax(result)

    return persion_disease[output_classes[class_num]]
