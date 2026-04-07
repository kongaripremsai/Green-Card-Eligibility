async function checkEligibility() {
    const data = {
        family_in_us: document.getElementById("family").checked,
        job_offer: document.getElementById("job").checked,
        education: document.getElementById("education").value,
        investment: parseFloat(document.getElementById("investment").value) || 0,
        refugee_status: document.getElementById("refugee").checked,
        country_in_dv_list: document.getElementById("dv").checked
    };

    const response = await fetch("http://127.0.0.1:8000/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText = result.result;
}