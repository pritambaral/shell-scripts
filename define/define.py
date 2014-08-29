import sys
from api import apiUrl,apiKey
from wordnik import swagger,WordApi

word = sys.argv[1];

#Initialise client
client = swagger.ApiClient(apiKey, apiUrl);

wordApi = WordApi.WordApi(client);
definitions = wordApi.getDefinitions(word,sourceDictionaries='wiktionary');
if not definitions:
	print "Trying for "+word.lower();
	definitions = wordApi.getDefinitions(word.lower(),sourceDictionaries='wiktionary');

for definition in definitions:
	print definition.partOfSpeech+": "+definition.text;
