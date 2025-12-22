/*const createBtn = document.getElementById('createBtn');
const saveBtn = document.getElementById('saveBtn');

createBtn.addEventListener('click', createTable);
saveBtn.addEventListener('click', saveData);

// Reset number input on page load
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('count').value = '';
    loadPartners(); // Load all partners initially
});

function createTable() {
    const num = parseInt(document.getElementById('count').value);
    if (!num || num <= 0) {
        alert('Please enter a valid number');
        return;
    }

    let html = '';
    for (let i = 1; i <= num; i++) {
        html += `<input type="text" id="name${i}" placeholder="Partner ${i}" style="display:block; width:100%; margin-bottom:10px;">`;
    }

    document.getElementById('nameFields').innerHTML = html;
    document.getElementById('step1').style.display = 'none';
    document.getElementById('step2').style.display = 'block';
}

function saveData() {
    const num = parseInt(document.getElementById('count').value);
    const partners = [];

    for (let i = 1; i <= num; i++) {
        const name = document.getElementById(`name${i}`).value.trim();
        partners.push({ name1: name });
    }

    frappe.call({
        method: 'library_management.library_management.api.save_partners',
        args: { partners: partners },
        callback: function(response) {
            if (response.message && response.message.success) {
                document.getElementById('message').innerText = `Saved ${response.message.count} partner(s).`;
                document.getElementById('step1').style.display = 'block';
                document.getElementById('step2').style.display = 'none';
                document.getElementById('count').value = '';
                loadPartners(); // Refresh list
            } else {
                document.getElementById('message').innerText = response.message.error;
            }
        }
    });
}

// Load all partners
function loadPartners() {
    frappe.call({
        method: 'library_management.library_management.api.get_partners',
        callback: function(response) {
            const tbody = document.getElementById('partnerList');
            tbody.innerHTML = '';
            response.message.forEach(p => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${p.name}</td>
                    <td><input type="text" value="${p.name1}" id="edit_${p.name}" style="width:90%"></td>
                    <td>
                        <button onclick="updatePartner('${p.name}')">Update</button>
                        <button onclick="deletePartner('${p.name}')">Delete</button>
                    </td>`;
                tbody.appendChild(tr);
            });
        }
    });
}

function updatePartner(partnerId) {
    const inputId = `edit_${safeId(partnerId)}`;
    const newName = document.getElementById(inputId).value.trim();

    if (!newName) {
        alert("Name cannot be empty!");
        return;
    }

    frappe.call({
        method: 'library_management.library_management.api.update_partner',
        args: { partner_id: partnerId, new_name: newName },
        callback: function(response) {
            if (response.message && response.message.success) {
                loadPartners(); // <-- reloads the table to show updated names
            } else {
                alert(response.message.error);
            }
        }
    });
}

}

function deletePartner(partnerId) {
    if (!confirm('Are you sure you want to delete this partner?')) return;
    frappe.call({
        method: 'library_management.library_management.api.delete_partner',
        args: { partner_id: partnerId },
        callback: function(response) {
            if (response.message && response.message.success) {
                loadPartners();
            } else {
                alert(response.message.error);
            }
        }
    });
} */
