document.getElementById('vcfForm').addEventListener('submit', function(e){
    e.preventDefault();

    const file = document.getElementById('vcfFile').files[0];
    const drug = document.getElementById('drugName').value;
    const patient_name = document.getElementById('patientName').value;
    const age = document.getElementById('age').value;
    const weight = document.getElementById('weight').value;

    const formData = new FormData();
    formData.append('vcf_file', file);
    formData.append('drug_name', drug);
    formData.append('patient_name', patient_name);
    formData.append('age', age);
    formData.append('weight', weight);

    fetch('http://127.0.0.1:5000/parse_vcf', {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if(data.error){
            document.getElementById('output').innerText = data.error;
            return;
        }

        let colorClass = '';
        switch(data.risk_assessment.risk_label){
            case 'Safe': colorClass='safe'; break;
            case 'Adjust Dosage': colorClass='adjust'; break;
            case 'Toxic': colorClass='toxic'; break;
            case 'Ineffective': colorClass='adjust'; break;
            default: colorClass=''; break;
        }

        document.getElementById('output').innerHTML =
            `<pre class="${colorClass}">${JSON.stringify(data,null,2)}</pre>`;
    })
    .catch(err => document.getElementById('output').innerText = 'Error: '+err);
});