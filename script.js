// IPL Team Generator Script
document.addEventListener('DOMContentLoaded', function() {
    const teamForm = document.getElementById('teamForm');
    const budgetSlider = document.getElementById('budget');
    const budgetValue = document.getElementById('budgetValue');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const loadingSteps = document.getElementById('loadingSteps');
    const resultsSection = document.getElementById('results');
    const generateBtn = document.querySelector('.generate-btn');
    const btnText = document.querySelector('.btn-text');
    const btnLoader = document.querySelector('.btn-loader');

    // Team color mappings
    const teamColors = {
        'CSK': 'team-CSK',
        'MI': 'team-MI',
        'RCB': 'team-RCB',
        'RR': 'team-RR',
        'LSG': 'team-LSG',
        'SRH': 'team-SRH',
        'PBKS': 'team-PBKS',
        'KKR': 'team-KKR',
        'ALL': ''
    };

    // Update budget display
    budgetSlider.addEventListener('input', function() {
        budgetValue.textContent = this.value;
    });

    // Apply team theme
    function applyTeamTheme(teamCode) {
        // Remove all team classes
        Object.values(teamColors).forEach(className => {
            if (className) document.body.classList.remove(className);
        });
        
        // Add selected team class
        if (teamColors[teamCode]) {
            document.body.classList.add(teamColors[teamCode]);
        }
    }

    // Team selection change handler
    document.getElementById('team').addEventListener('change', function() {
        applyTeamTheme(this.value);
    });

    // Loading animation steps
    const loadingStepsData = [
        "🔄 Applying Salp Chain Optimization...",
        "🐟 Running Tuna Swarm Optimization...",
        "🔗 Executing Remora Optimization...",
        "⚖️ Balancing team composition...",
        "💰 Optimizing budget allocation...",
        "🏆 Finalizing your dream team..."
    ];

    // Show loading animation
    function showLoading() {
        loadingOverlay.style.display = 'flex';
        generateBtn.disabled = true;
        btnText.textContent = 'Generating...';
        btnLoader.style.display = 'inline-block';

        let stepIndex = 0;
        const stepInterval = setInterval(() => {
            if (stepIndex < loadingStepsData.length) {
                loadingSteps.innerHTML = `<div class="step">${loadingStepsData[stepIndex]}</div>`;
                stepIndex++;
            } else {
                clearInterval(stepInterval);
            }
        }, 800);

        return stepInterval;
    }

    // Hide loading animation
    function hideLoading(stepInterval) {
        clearInterval(stepInterval);
        loadingOverlay.style.display = 'none';
        generateBtn.disabled = false;
        btnText.textContent = 'Generate Best Team';
        btnLoader.style.display = 'none';
    }

    // Generate team data (simulating the Python backend)
    function generateTeamData(teamCode, budget) {
        return new Promise((resolve) => {
            // Simulate API call delay
            setTimeout(() => {
                const mockTeamData = generateMockTeamData(teamCode, budget);
                resolve(mockTeamData);
            }, 5000);
        });
    }

    // Mock team data generator (since we don't have a backend)
    function generateMockTeamData(teamCode, budget) {
        // Sample player data
        const samplePlayers = [
            { Name: "Virat Kohli", Role: "Top-order Batsman", Team: "RCB", Performance_Score: 89.5, Cost: 12.5 },
            { Name: "Jasprit Bumrah", Role: "Pacer", Team: "MI", Performance_Score: 90.2, Cost: 11.8 },
            { Name: "MS Dhoni", Role: "Wicketkeeper", Team: "CSK", Performance_Score: 85.3, Cost: 10.2 },
            { Name: "Ravindra Jadeja", Role: "All-Rounder", Team: "CSK", Performance_Score: 88.7, Cost: 11.0 },
            { Name: "Suryakumar Yadav", Role: "Middle-order Batsman", Team: "MI", Performance_Score: 87.9, Cost: 10.8 },
            { Name: "Yashasvi Jaiswal", Role: "Top-order Batsman", Team: "RR", Performance_Score: 86.4, Cost: 9.5 },
            { Name: "Heinrich Klaasen", Role: "Wicketkeeper", Team: "SRH", Performance_Score: 84.2, Cost: 9.8 },
            { Name: "Hardik Pandya", Role: "All-Rounder", Team: "MI", Performance_Score: 85.6, Cost: 10.5 },
            { Name: "Mohammed Siraj", Role: "Pacer", Team: "RCB", Performance_Score: 82.3, Cost: 8.9 },
            { Name: "Rashid Khan", Role: "Spinner", Team: "SRH", Performance_Score: 88.1, Cost: 10.3 },
            { Name: "Shubman Gill", Role: "Top-order Batsman", Team: "GT", Performance_Score: 85.7, Cost: 9.2 }
        ];

        // Filter players based on team selection
        let availablePlayers = teamCode === 'ALL' ? samplePlayers : samplePlayers.filter(p => p.Team === teamCode);
        
        // If team-specific selection doesn't have enough players, add some from other teams
        if (availablePlayers.length < 11) {
            const additionalPlayers = samplePlayers.filter(p => !availablePlayers.includes(p));
            availablePlayers = [...availablePlayers, ...additionalPlayers].slice(0, 15);
        }

        // Select 11 players within budget
        const selectedPlayers = selectPlayersWithinBudget(availablePlayers, budget);
        
        const totalCost = selectedPlayers.reduce((sum, player) => sum + player.Cost, 0);
        const totalPerformance = selectedPlayers.reduce((sum, player) => sum + player.Performance_Score, 0);
        
        // Calculate role distribution
        const roleDistribution = {};
        selectedPlayers.forEach(player => {
            roleDistribution[player.Role] = (roleDistribution[player.Role] || 0) + 1;
        });

        return {
            team: selectedPlayers,
            total_cost: Math.round(totalCost * 100) / 100,
            total_performance: Math.round(totalPerformance * 100) / 100,
            role_distribution: roleDistribution,
            target_team: teamCode,
            budget: budget
        };
    }

    // Select players within budget
    function selectPlayersWithinBudget(players, budget) {
        // Sort players by performance/cost ratio
        const sortedPlayers = players.sort((a, b) => (b.Performance_Score / b.Cost) - (a.Performance_Score / a.Cost));
        
        const selected = [];
        let remainingBudget = budget;
        
        // Ensure we have at least one of each key role
        const requiredRoles = ['Wicketkeeper', 'All-Rounder'];
        
        for (const role of requiredRoles) {
            const rolePlayer = sortedPlayers.find(p => p.Role === role && p.Cost <= remainingBudget && !selected.includes(p));
            if (rolePlayer) {
                selected.push(rolePlayer);
                remainingBudget -= rolePlayer.Cost;
            }
        }
        
        // Fill remaining spots
        for (const player of sortedPlayers) {
            if (selected.length >= 11) break;
            if (!selected.includes(player) && player.Cost <= remainingBudget) {
                selected.push(player);
                remainingBudget -= player.Cost;
            }
        }
        
        // If we still don't have 11 players, add cheapest available
        while (selected.length < 11 && selected.length < sortedPlayers.length) {
            const cheapestAvailable = sortedPlayers
                .filter(p => !selected.includes(p))
                .sort((a, b) => a.Cost - b.Cost)[0];
            
            if (cheapestAvailable) {
                selected.push(cheapestAvailable);
            } else {
                break;
            }
        }
        
        return selected.slice(0, 11);
    }

    // Display results
    function displayResults(teamData) {
        const teamName = teamData.target_team === 'ALL' ? 'Mixed Squad' : teamData.target_team;
        
        resultsSection.innerHTML = `
            <div class="team-summary fade-in">
                <div class="summary-header">
                    <h2 class="team-name">${teamName} - Optimized Team</h2>
                    <div class="summary-stats">
                        <div class="stat-item">
                            <span class="stat-value">₹${teamData.total_cost}</span>
                            <span class="stat-label">Total Cost (Crores)</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-value">${teamData.total_performance}</span>
                            <span class="stat-label">Total Performance</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-value">${teamData.team.length}</span>
                            <span class="stat-label">Players Selected</span>
                        </div>
                    </div>
                </div>
                
                <div class="role-distribution">
                    ${Object.entries(teamData.role_distribution).map(([role, count]) => `
                        <div class="role-item">
                            <div class="role-name">${role}</div>
                            <div class="role-count">${count}</div>
                        </div>
                    `).join('')}
                </div>
            </div>
            
            <div class="players-grid">
                ${teamData.team.map((player, index) => `
                    <div class="player-card" style="animation-delay: ${index * 0.1}s">
                        <div class="player-header">
                            <div>
                                <div class="player-name">${player.Name}</div>
                                <div class="player-role">${player.Role}</div>
                            </div>
                            <div class="player-team">${player.Team}</div>
                        </div>
                        <div class="player-stats">
                            <div class="stat">
                                <span class="stat-number">${player.Performance_Score}</span>
                                <span class="stat-text">Performance</span>
                            </div>
                            <div class="stat">
                                <span class="stat-number">₹${player.Cost}</span>
                                <span class="stat-text">Cost (Cr)</span>
                            </div>
                            <div class="stat">
                                <span class="stat-number">${Math.round(player.Performance_Score / player.Cost * 10) / 10}</span>
                                <span class="stat-text">Value Ratio</span>
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    // Form submission handler
    teamForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const teamCode = formData.get('team');
        const budget = parseFloat(formData.get('budget'));
        
        const stepInterval = showLoading();
        
        try {
            const teamData = await generateTeamData(teamCode, budget);
            hideLoading(stepInterval);
            displayResults(teamData);
        } catch (error) {
            console.error('Error generating team:', error);
            hideLoading(stepInterval);
            alert('Error generating team. Please try again.');
        }
    });

    // Initialize with default theme
    applyTeamTheme('ALL');
    
    // Add floating particles effect
    createFloatingParticles();
});

// Floating particles animation
function createFloatingParticles() {
    const particlesContainer = document.getElementById('particles-background');
    
    for (let i = 0; i < 20; i++) {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: absolute;
            width: ${Math.random() * 4 + 2}px;
            height: ${Math.random() * 4 + 2}px;
            background: var(--primary-color);
            border-radius: 50%;
            opacity: ${Math.random() * 0.5 + 0.3};
            animation: float ${Math.random() * 10 + 10}s linear infinite;
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            filter: blur(1px);
        `;
        particlesContainer.appendChild(particle);
    }
    
    // Add CSS animation for floating particles
    const style = document.createElement('style');
    style.textContent = `
        @keyframes float {
            0% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
            100% { transform: translateY(0px) rotate(360deg); }
        }
    `;
    document.head.appendChild(style);
}