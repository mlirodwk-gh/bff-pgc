from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- BFF Endpoints ---
@app.route('/bffpgc/v1/get_user_cns/<user_id>', methods=['GET'])
def get_user_all_consent(user_id):
    if user_id == "1":
        user_consents = [{"cmp_consent":{"creditos_vivienda":"true","operaciones_financieras":"true"}},{"cmp_consent_expiry":{"creditos_vivienda":"2026-10-24T00:00:00.000Z","operaciones_financieras":"2026-10-24T00:00:00.000Z"}},{"cmp_records":[{"id":"record_1761083557380","userId":"user_w2xgzuvl4","timestamp":"2025-10-21T21:52:37.380Z","consents":{"operaciones_financieras":"true"},"consentExpiry":{"operaciones_financieras":"2026-10-22T00:00:00.000Z"},"ipAddress":"192.168.1.1","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}]}]
        return jsonify(user_consents),200
    else:
        return jsonify({"message": "User not found"}), 404

# --- BFF Endpoints ---
@app.route('/bffpgc/v1/save_user_cns', methods=['POST'])
def save_user_consent():
        print(request.data)
        resp = ""
        try:
             req_data = request.get_json()
             user_id = req_data["userId"]
             resp = jsonify({"recordId":"000001","message": f"Consentimientos registrados OK para usuario {user_id}"})
        except Exception as error:
             print(error)
        if resp == "":
             resp = jsonify({"recordId":"","message": "Error al tratar de registrar los consentimientos"})
        return resp,200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=3000)