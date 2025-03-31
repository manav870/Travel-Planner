// Main JavaScript file for Travel Planner

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips if Bootstrap is loaded
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });

        // Auto-dismiss alerts after 5 seconds
        const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
        alerts.forEach(function(alert) {
            setTimeout(function() {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 5000);
        });
    }

    // Add hover effect to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Date validation for trip planning
    const startDateInput = document.getElementById('start_date');
    const endDateInput = document.getElementById('end_date');
    
    if (startDateInput && endDateInput) {
        // Set minimum date to today
        const today = new Date().toISOString().split('T')[0];
        startDateInput.min = today;
        endDateInput.min = today;
        
        // Update end_date min when start_date changes
        startDateInput.addEventListener('change', function() {
            endDateInput.min = this.value;
            if (endDateInput.value && endDateInput.value < this.value) {
                endDateInput.value = this.value;
            }
        });
    }
    
    // Suggested Budget functionality
    const destinationSelect = document.getElementById('destination');
    const suggestedBudgetInline = document.getElementById('suggested-budget-inline');
    const budgetWarning = document.getElementById('budget-warning');
    
    if (destinationSelect && suggestedBudgetInline) {
        // Destination budget data
        const destinationBudgets = {
            '1': { name: 'Paris', min: 1200, max: 2000 },
            '2': { name: 'Tokyo', min: 1500, max: 2500 },
            '3': { name: 'New York', min: 1800, max: 3000 },
            '4': { name: 'Rome', min: 1000, max: 1800 },
            '5': { name: 'Bali', min: 800, max: 1500 },
            '6': { name: 'London', min: 1500, max: 2500 },
            '7': { name: 'Sydney', min: 1600, max: 2700 }
        };
        
        const budgetInput = document.getElementById('budget');
        let currentDestination = null;
        
        destinationSelect.addEventListener('change', function() {
            const destinationId = this.value;
            if (destinationId && destinationBudgets[destinationId]) {
                currentDestination = destinationBudgets[destinationId];
                
                // Update inline suggestion
                document.getElementById('budget-min-inline').textContent = currentDestination.min;
                document.getElementById('budget-max-inline').textContent = currentDestination.max;
                suggestedBudgetInline.classList.remove('d-none');
                
                // Update budget input with suggested minimum value
                if (budgetInput && !budgetInput.value) {
                    budgetInput.value = currentDestination.min;
                }
                
                // Check if current budget is below minimum
                checkBudget();
            } else {
                currentDestination = null;
                suggestedBudgetInline.classList.add('d-none');
                budgetWarning.classList.add('d-none');
            }
        });
        
        // Add input event listener to budget field
        if (budgetInput) {
            budgetInput.addEventListener('input', checkBudget);
        }
        
        // Function to check budget and show/hide warning
        function checkBudget() {
            if (!currentDestination || !budgetInput.value) {
                budgetWarning.classList.add('d-none');
                return;
            }
            
            const budgetValue = parseInt(budgetInput.value);
            // Check if the value is a valid number
            if (isNaN(budgetValue)) {
                budgetWarning.classList.add('d-none');
                return;
            }
            
            if (budgetValue < currentDestination.min) {
                // Show warning
                document.getElementById('warning-min-amount').textContent = currentDestination.min;
                document.getElementById('warning-destination').textContent = currentDestination.name;
                budgetWarning.classList.remove('d-none');
            } else {
                // Hide warning
                budgetWarning.classList.add('d-none');
            }
        }
    }
}); 