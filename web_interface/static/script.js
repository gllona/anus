// ANUS Web Interface - JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const menuItems = document.querySelectorAll('.menu-item');
    const contentSections = document.querySelectorAll('.content-section');
    const taskInput = document.getElementById('task-input');
    const submitButton = document.getElementById('submit-task');
    const modeRadios = document.querySelectorAll('input[name="mode"]');
    const loadingIndicator = document.getElementById('loading');
    const responseText = document.getElementById('response-text');
    const complexityValue = document.getElementById('complexity-value');
    const modeValue = document.getElementById('mode-value');
    const historyContainer = document.getElementById('history-container');
    const saveSettingsButton = document.getElementById('save-settings');
    
    // Initialize the application
    init();
    
    function init() {
        // Add event listeners
        addNavigationListeners();
        addTaskSubmissionListener();
        addSettingsSaveListener();
        
        // Load history if on history tab
        if (document.getElementById('section-history').classList.contains('active')) {
            loadHistory();
        }
    }
    
    function addNavigationListeners() {
        menuItems.forEach(item => {
            item.addEventListener('click', () => {
                const targetId = item.id.replace('nav-', 'section-');
                
                // Update active menu item
                menuItems.forEach(mi => mi.classList.remove('active'));
                item.classList.add('active');
                
                // Show selected content section
                contentSections.forEach(section => {
                    section.classList.remove('active');
                    if (section.id === targetId) {
                        section.classList.add('active');
                        
                        // Load history if navigating to history tab
                        if (targetId === 'section-history') {
                            loadHistory();
                        }
                    }
                });
            });
        });
    }
    
    function addTaskSubmissionListener() {
        submitButton.addEventListener('click', () => {
            const task = taskInput.value.trim();
            if (!task) {
                showNotification('Please enter a task', 'error');
                return;
            }
            
            // Get selected mode
            let selectedMode = 'auto';
            modeRadios.forEach(radio => {
                if (radio.checked) {
                    selectedMode = radio.value;
                }
            });
            
            executeTask(task, selectedMode);
        });
    }
    
    function addSettingsSaveListener() {
        saveSettingsButton.addEventListener('click', () => {
            const apiKey = document.getElementById('api-key').value;
            const model = document.getElementById('model-select').value;
            const verbose = document.getElementById('verbose-mode').checked;
            
            // In a real application, you would save these settings to a backend or localStorage
            // For now, we'll just show a notification
            showNotification('Settings saved successfully', 'success');
            
            console.log('Settings saved:', { apiKey, model, verbose });
        });
    }
    
    function executeTask(task, mode) {
        // Show loading indicator
        loadingIndicator.style.display = 'block';
        responseText.textContent = '';
        complexityValue.textContent = 'Calculating...';
        modeValue.textContent = 'Determining...';
        
        // Prepare request data
        const requestData = {
            task: task,
            mode: mode
        };
        
        // Send request to API
        fetch('/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading indicator
            loadingIndicator.style.display = 'none';
            
            if (data.success) {
                // Update response area
                responseText.textContent = data.result;
                complexityValue.textContent = data.task_complexity || 'N/A';
                modeValue.textContent = data.mode_used || mode;
                
                // Add to history (in a real app, this would be handled by the backend)
                addToHistory(task, data.result);
            } else {
                responseText.textContent = `Error: ${data.error || 'Unknown error occurred'}`;
                showNotification('Failed to execute task', 'error');
            }
        })
        .catch(error => {
            // Hide loading indicator
            loadingIndicator.style.display = 'none';
            
            // Show error
            responseText.textContent = `Error: ${error.message}`;
            showNotification('An error occurred while communicating with the server', 'error');
            console.error('Error executing task:', error);
        });
    }
    
    function loadHistory() {
        historyContainer.innerHTML = '<p class="text-center">Loading history...</p>';
        
        fetch('/history')
            .then(response => response.json())
            .then(data => {
                if (data.success && data.history) {
                    renderHistory(data.history);
                } else {
                    historyContainer.innerHTML = '<p class="text-center">Failed to load history</p>';
                }
            })
            .catch(error => {
                historyContainer.innerHTML = '<p class="text-center">Error loading history</p>';
                console.error('Error loading history:', error);
            });
    }
    
    function renderHistory(historyItems) {
        if (historyItems.length === 0) {
            historyContainer.innerHTML = '<p class="text-center">No history available</p>';
            return;
        }
        
        let historyHTML = '';
        historyItems.forEach(item => {
            historyHTML += `
                <div class="history-item">
                    <div class="history-task">${item.task}</div>
                    <div class="history-result">${item.result}</div>
                </div>
            `;
        });
        
        historyContainer.innerHTML = historyHTML;
    }
    
    function addToHistory(task, result) {
        // This is a client-side simulation of history for demo purposes
        // In a real application, history would be stored in a database
        
        // We don't actually do anything here since we're not persisting data in this demo
        console.log('Added to history:', { task, result });
    }
    
    function showNotification(message, type = 'info') {
        // In a real application, you would show a toast notification
        // For now, we'll just log to console
        console.log(`[${type}] ${message}`);
        
        // Alternative: create a simple alert if needed
        // alert(message);
    }
}); 