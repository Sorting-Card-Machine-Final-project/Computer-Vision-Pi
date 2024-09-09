document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('start-btn').addEventListener('click', () => {
        fetch('/start_process', { method: 'POST' })
            .then(response => response.json())
            .then(data => updateLogs(data.status));
    });

    document.getElementById('stop-btn').addEventListener('click', () => {
        fetch('/stop_process', { method: 'POST' })
            .then(response => response.json())
            .then(data => updateLogs(data.status));
    });

    // Fetch logs and deck order every 2 seconds
    setInterval(fetchLogsAndDeckOrder, 2000);

    function fetchLogsAndDeckOrder() {
        // Fetch logs
        fetch('/get_logs')
            .then(response => response.json())
            .then(logs => {
                const logContainer = document.getElementById('log-container');
                logContainer.innerHTML = '';  // Clear old logs
                logs.forEach(log => {
                    const logEntry = document.createElement('p');
                    logEntry.textContent = log;
                    logContainer.appendChild(logEntry);
                });
            });

        // Fetch deck order
        fetch('/get_deck_order')
            .then(response => response.json())
            .then(deckOrder => {
                const deckOrderContainer = document.getElementById('deck-order-container');
                deckOrderContainer.innerHTML = '';  // Clear old entries
                deckOrder.forEach(card => {
                    const cardEntry = document.createElement('p');
                    cardEntry.textContent = card;
                    deckOrderContainer.appendChild(cardEntry);
                });
            });
    }

    function updateLogs(message) {
        const logContainer = document.getElementById('log-container');
        const logEntry = document.createElement('p');
        logEntry.textContent = message;
        logContainer.appendChild(logEntry);
    }
});
