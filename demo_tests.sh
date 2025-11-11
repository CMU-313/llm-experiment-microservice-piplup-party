#!/bin/bash

echo "=========================================="
echo "  Translation Service Demo Tests"
echo "=========================================="
echo ""

# Test 1: English
echo "Test 1: English Text"
echo "Input: Hello world"
curl -s "http://localhost:8080/translate?content=Hello%20world" | python3 -m json.tool
echo ""
echo "---"
echo ""

# Test 2: Spanish
echo "Test 2: Spanish"
echo "Input: Hola mundo como estas"
curl -s "http://localhost:8080/translate?content=Hola%20mundo%20como%20estas" | python3 -m json.tool
echo ""
echo "---"
echo ""

# Test 3: German
echo "Test 3: German"
echo "Input: Hier ist dein erstes Beispiel"
curl -s "http://localhost:8080/translate?content=Hier%20ist%20dein%20erstes%20Beispiel" | python3 -m json.tool
echo ""
echo "---"
echo ""

# Test 4: French
echo "Test 4: French"
echo "Input: Bonjour tout le monde"
curl -s "http://localhost:8080/translate?content=Bonjour%20tout%20le%20monde" | python3 -m json.tool
echo ""
echo "---"
echo ""

# Test 5: Japanese (POST)
echo "Test 5: Japanese"
echo "Input: 情報 システムを勉強しています"
curl -s -X POST http://localhost:8080/translate -H "Content-Type: application/json" -d '{"content":"情報 システムを勉強しています"}' | python3 -m json.tool
echo ""
echo "---"
echo ""

# Test 6: Chinese (POST)
echo "Test 6: Chinese"
echo "Input: 你好世界"
curl -s -X POST http://localhost:8080/translate -H "Content-Type: application/json" -d '{"content":"你好世界"}' | python3 -m json.tool
echo ""
echo "---"
echo ""

# Test 7: Arabic (POST)
echo "Test 7: Arabic"
echo "Input: مرحبا بالعالم"
curl -s -X POST http://localhost:8080/translate -H "Content-Type: application/json" -d '{"content":"مرحبا بالعالم"}' | python3 -m json.tool
echo ""
echo "---"
echo ""

# Test 8: Russian (POST)
echo "Test 8: Russian"
echo "Input: Привет мир"
curl -s -X POST http://localhost:8080/translate -H "Content-Type: application/json" -d '{"content":"Привет мир"}' | python3 -m json.tool
echo ""
echo "=========================================="
echo "  All Tests Complete!"
echo "=========================================="

