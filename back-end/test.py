from llama_cpp import Llama

model_path='/Users/gianni/Progetti/LLM Models/mistral-7b-instruct-v0.1.Q4_K_M.gguf'

model = Llama(model_path = model_path,
              n_ctx = 2048,            # context window size
              n_gpu_layers = 1,        # enable GPU
              use_mlock = True)        # enable memory lock so not swap


prompt = """
[INST]<<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.

Given the following patient information JSON, create a human-readable sentence describing the patient:

{
  "resourceType": "Patient",
  "id": "30163",
  "meta": {
    "versionId": "7",
    "lastUpdated": "2023-03-17T07:19:18.297+00:00",
    "source": "#9uydlZucYM7rIcfE",
    "profile": [ "http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-patient" ]
  },
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Sabine Muster </b> female, DoB: 1930-03-06 ( Social Security Number: 756823476)</p></div>"
  },
  "extension": [ {
    "url": "http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-ext-patient-religion",
    "extension": [ {
      "url": "code",
      "valueCodeableConcept": {
        "coding": [ {
          "system": "http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/CodeSystem/at-core-cs-religion",
          "code": "162",
          "display": "Pastafarianismus"
        } ]
      }
    } ]
  }, {
    "url": "http://hl7.org/fhir/StructureDefinition/patient-citizenship",
    "extension": [ {
      "url": "code",
      "valueCodeableConcept": {
        "coding": [ {
          "system": "http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/CodeSystem/at-core-cs-iso-3166-1-alpha-3",
          "code": "AUT",
          "display": "Österreich"
        } ]
      }
    } ]
  } ],
  "identifier": [ {
    "type": {
      "coding": [ {
        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
        "code": "SS",
        "display": "Social Security Number"
      } ]
    },
    "system": "urn:oid:1.2.40.0.10.1.4.3.1",
    "value": "756823476",
    "assigner": {
      "display": "Dachverband der österreichischen Sozialversicherungsträger"
    }
  }, {
    "type": {
      "coding": [ {
        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
        "code": "NI",
        "display": "National unique individual identifier"
      } ]
    },
    "system": "urn:oid:1.2.40.0.10.2.1.1.149",
    "value": "GH:oeLdSEb0l+8kSdJWjOYyYmnYki0=",
    "assigner": {
      "display": "Bundesministerium für Inneres"
    }
  }, {
    "type": {
      "coding": [ {
        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
        "code": "PI",
        "display": "Patient internal identifier"
      } ]
    },
    "system": "urn:oid:1.2.3.4.5",
    "value": "2936",
    "assigner": {
      "display": "Ein GDA in Österreich"
    }
  } ],
  "name": [ {
    "family": "Brown",
    "given": [ "Thomas" ],
    "prefix": [ "Mr" ]
  } ],
  "telecom": [ {
    "system": "email",
    "value": "office@hl7.at",
    "use": "work"
  }, {
    "system": "phone",
    "value": "+43650123534890",
    "use": "home"
  } ],
  "gender": "female",
  "birthDate": "1930-03-06",
  "address": [ {
    "use": "home",
    "type": "both",
    "line": [ "Landstrasse 5 Stock 3 Tür 26" ],
    "_line": [ {
      "extension": [ {
        "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-streetName",
        "valueString": "Landstrasse"
      }, {
        "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber",
        "valueString": "5"
      }, {
        "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-additionalLocator",
        "valueString": "Stock 3 Tür 26"
      }, {
        "url": "http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-ext-address-additionalInformation",
        "valueString": "Lift vorhanden"
      } ]
    } ],
    "city": "Linz",
    "state": "Oberösterreich",
    "postalCode": "4020",
    "country": "AUT"
  } ]
}

Create a sentence that includes the patient's information.
[/INST]
"""

output = model(prompt = prompt, max_tokens = 120, temperature = 0.2)
print(output['choices'][0]['text'])