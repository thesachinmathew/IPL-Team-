import random
import math
import webbrowser
import os
from typing import List, Dict, Tuple
import json

ipl_players = [
    {"Name": "Ruturaj Gaikwad", "Role": "Top-order Batsman", "Team": "CSK", "Ranking": 45},
    {"Name": "MS Dhoni", "Role": "Wicketkeeper", "Team": "CSK", "Ranking": 91},
    {"Name": "Ravindra Jadeja", "Role": "All-Rounder", "Team": "CSK", "Ranking": 58},
    {"Name": "Moeen Ali", "Role": "All-Rounder", "Team": "CSK", "Ranking": 67},
    {"Name": "Deepak Chahar", "Role": "Pacer", "Team": "CSK", "Ranking": 77},
    {"Name": "Matheesha Pathirana", "Role": "Pacer", "Team": "CSK", "Ranking": 85},
    {"Name": "Shivam Dube", "Role": "Middle-order Batsman", "Team": "CSK", "Ranking": 62},

    {"Name": "Rohit Sharma", "Role": "Top-order Batsman", "Team": "MI", "Ranking": 93},
    {"Name": "Ishan Kishan", "Role": "Wicketkeeper", "Team": "MI", "Ranking": 41},
    {"Name": "Suryakumar Yadav", "Role": "Middle-order Batsman", "Team": "MI", "Ranking": 88},
    {"Name": "Tilak Varma", "Role": "Middle-order Batsman", "Team": "MI", "Ranking": 59},
    {"Name": "Jasprit Bumrah", "Role": "Pacer", "Team": "MI", "Ranking": 96},
    {"Name": "Gerald Coetzee", "Role": "Pacer", "Team": "MI", "Ranking": 53},
    {"Name": "Hardik Pandya", "Role": "All-Rounder", "Team": "MI", "Ranking": 72},

    {"Name": "Virat Kohli", "Role": "Top-order Batsman", "Team": "RCB", "Ranking": 95},
    {"Name": "Faf du Plessis", "Role": "Top-order Batsman", "Team": "RCB", "Ranking": 86},
    {"Name": "Glenn Maxwell", "Role": "All-Rounder", "Team": "RCB", "Ranking": 76},
    {"Name": "Dinesh Karthik", "Role": "Wicketkeeper", "Team": "RCB", "Ranking": 55},
    {"Name": "Mohammed Siraj", "Role": "Pacer", "Team": "RCB", "Ranking": 66},
    {"Name": "Reece Topley", "Role": "Pacer", "Team": "RCB", "Ranking": 44},
    {"Name": "Cameron Green", "Role": "All-Rounder", "Team": "RCB", "Ranking": 73},

    {"Name": "Sanju Samson", "Role": "Wicketkeeper", "Team": "RR", "Ranking": 71},
    {"Name": "Jos Buttler", "Role": "Top-order Batsman", "Team": "RR", "Ranking": 84},
    {"Name": "Yashasvi Jaiswal", "Role": "Top-order Batsman", "Team": "RR", "Ranking": 90},
    {"Name": "Riyan Parag", "Role": "Middle-order Batsman", "Team": "RR", "Ranking": 60},
    {"Name": "R Ashwin", "Role": "Spinner", "Team": "RR", "Ranking": 63},
    {"Name": "Trent Boult", "Role": "Pacer", "Team": "RR", "Ranking": 78},
    {"Name": "Shimron Hetmyer", "Role": "Middle-order Batsman", "Team": "RR", "Ranking": 57},

    {"Name": "KL Rahul", "Role": "Top-order Batsman", "Team": "LSG", "Ranking": 94},
    {"Name": "Nicholas Pooran", "Role": "Wicketkeeper", "Team": "LSG", "Ranking": 47},
    {"Name": "Marcus Stoinis", "Role": "All-Rounder", "Team": "LSG", "Ranking": 50},
    {"Name": "Ravi Bishnoi", "Role": "Spinner", "Team": "LSG", "Ranking": 65},
    {"Name": "Naveen-ul-Haq", "Role": "Pacer", "Team": "LSG", "Ranking": 56},
    {"Name": "Krunal Pandya", "Role": "All-Rounder", "Team": "LSG", "Ranking": 43},
    {"Name": "Deepak Hooda", "Role": "Middle-order Batsman", "Team": "LSG", "Ranking": 54},

    {"Name": "Abhishek Sharma", "Role": "Top-order Batsman", "Team": "SRH", "Ranking": 80},
    {"Name": "Heinrich Klaasen", "Role": "Wicketkeeper", "Team": "SRH", "Ranking": 97},
    {"Name": "Aiden Markram", "Role": "Middle-order Batsman", "Team": "SRH", "Ranking": 82},
    {"Name": "Bhuvneshwar Kumar", "Role": "Pacer", "Team": "SRH", "Ranking": 52},
    {"Name": "Pat Cummins", "Role": "Pacer", "Team": "SRH", "Ranking": 46},
    {"Name": "Rahul Tripathi", "Role": "Middle-order Batsman", "Team": "SRH", "Ranking": 49},
    {"Name": "Washington Sundar", "Role": "Spinner", "Team": "SRH", "Ranking": 64},

    {"Name": "Shikhar Dhawan", "Role": "Top-order Batsman", "Team": "PBKS", "Ranking": 89},
    {"Name": "Jitesh Sharma", "Role": "Wicketkeeper", "Team": "PBKS", "Ranking": 74},
    {"Name": "Liam Livingstone", "Role": "All-Rounder", "Team": "PBKS", "Ranking": 81},
    {"Name": "Arshdeep Singh", "Role": "Pacer", "Team": "PBKS", "Ranking": 48},
    {"Name": "Kagiso Rabada", "Role": "Pacer", "Team": "PBKS", "Ranking": 61},
    {"Name": "Sam Curran", "Role": "All-Rounder", "Team": "PBKS", "Ranking": 68},
    {"Name": "Harpreet Brar", "Role": "Spinner", "Team": "PBKS", "Ranking": 42},

    # Kolkata Knight Riders (KKR)
    {"Name": "Shreyas Iyer", "Role": "Middle-order Batsman", "Team": "KKR", "Ranking": 87},
    {"Name": "Andre Russell", "Role": "All-Rounder", "Team": "KKR", "Ranking": 70},
    {"Name": "Rinku Singh", "Role": "Middle-order Batsman", "Team": "KKR", "Ranking": 83},
    {"Name": "Rahmanullah Gurbaz", "Role": "Wicketkeeper", "Team": "KKR", "Ranking": 75},
    {"Name": "Sunil Narine", "Role": "Spinner", "Team": "KKR", "Ranking": 51},
    {"Name": "Varun Chakravarthy", "Role": "Spinner", "Team": "KKR", "Ranking": 69},
    {"Name": "Mitchell Starc", "Role": "Pacer", "Team": "KKR", "Ranking": 92}
]

class SalpChainOptimization:
    def __init__(self, players: List[Dict], budget: float):
        self.players = players
        self.budget = budget
        self.population_size = 30
        self.max_iterations = 50
        
    def optimize_performance_scores(self) -> List[Dict]:
        enhanced_players = []
        
        for player in self.players:
            salp_chain = [random.uniform(0.8, 1.2) for _ in range(self.population_size)]
            
            best_multiplier = 1.0
            best_score = player["Ranking"]
            
            for iteration in range(self.max_iterations):
                for i in range(self.population_size):
                    if i == 0:
                        c1 = 2 * math.exp(-(4 * iteration / self.max_iterations) ** 2)
                        salp_chain[i] = random.uniform(0.8, 1.2) * c1
                    else:
                        salp_chain[i] = (salp_chain[i] + salp_chain[i-1]) / 2
                
                for multiplier in salp_chain:
                    enhanced_score = player["Ranking"] * multiplier
                    if enhanced_score > best_score and enhanced_score <= 100:
                        best_score = enhanced_score
                        best_multiplier = multiplier
            
            enhanced_player = player.copy()
            enhanced_player["Performance_Score"] = round(best_score, 2)
            enhanced_player["Cost"] = self._calculate_cost(enhanced_player)
            enhanced_players.append(enhanced_player)
        
        return enhanced_players
    
    def _calculate_cost(self, player: Dict) -> float:
        base_cost = (player["Performance_Score"] / 15) + random.uniform(1, 3)
        role_multiplier = {
            "Top-order Batsman": 1.1,
            "Middle-order Batsman": 1.0,
            "Wicketkeeper": 1.2,
            "All-Rounder": 1.3,
            "Spinner": 0.9,
            "Pacer": 1.0
        }
        
        final_cost = base_cost * role_multiplier.get(player["Role"], 1.0)
        
        # Ensure costs are within reasonable bounds (2-15 crores)
        final_cost = max(2.0, min(15.0, final_cost))
        
        return round(final_cost, 2)

class TunaSwarmOptimization:
    def __init__(self, players: List[Dict], budget: float):
        self.players = players
        self.budget = budget
        self.swarm_size = 30
        self.max_iterations = 60
        
    def select_players(self) -> List[Dict]:
        self.players.sort(key=lambda x: x["Performance_Score"] / x["Cost"], reverse=True)
        
        best_solution = None
        best_fitness = -1
        
        for attempt in range(100):  # Multiple attempts to find valid solution
            swarm = []
            for _ in range(self.swarm_size):
                solution = self._create_valid_initial_solution()
                swarm.append(solution)
            
            for iteration in range(self.max_iterations):
                for i, tuna in enumerate(swarm):
                    # Ensure solution is valid
                    tuna = self._repair_solution(tuna)
                    
                    fitness = self._evaluate_fitness(tuna)
                    if fitness > best_fitness:
                        best_fitness = fitness
                        best_solution = tuna.copy()
                    
                    # Apply tuna swarm behaviors
                    if random.random() < 0.7:
                        tuna = self._spiral_behavior(tuna, best_solution if best_solution else tuna)
                    else:
                        tuna = self._straight_behavior(tuna)
                    
                    swarm[i] = self._repair_solution(tuna)
            
            # If we found a valid solution, break
            if best_solution and self._is_valid_solution(best_solution):
                break
        
        # If no valid solution found, use greedy approach
        if not best_solution or not self._is_valid_solution(best_solution):
            best_solution = self._greedy_selection()
        
        selected_players = []
        for i, selected in enumerate(best_solution):
            if selected and i < len(self.players):
                selected_players.append(self.players[i])
        
        return selected_players[:11]  # Ensure exactly 11 players
    
    def _create_valid_initial_solution(self) -> List[int]:
        """Create an initial solution that respects budget constraints"""
        solution = [0] * len(self.players)
        selected_players = []
        current_cost = 0
        
        # Sort players by value for money within budget
        affordable_players = [(i, p) for i, p in enumerate(self.players) if p["Cost"] <= self.budget]
        affordable_players.sort(key=lambda x: x[1]["Performance_Score"] / x[1]["Cost"], reverse=True)
        
        for i, player in affordable_players:
            if len(selected_players) >= 11:
                break
            if current_cost + player["Cost"] <= self.budget:
                solution[i] = 1
                selected_players.append(player)
                current_cost += player["Cost"]
        
        return solution
    
    def _repair_solution(self, solution: List[int]) -> List[int]:
        """Repair solution to meet constraints"""
        selected_indices = [i for i, val in enumerate(solution) if val == 1]
        
        # Remove players until budget is satisfied
        while selected_indices:
            total_cost = sum(self.players[i]["Cost"] for i in selected_indices if i < len(self.players))
            if total_cost <= self.budget:
                break
            
            # Remove the player with worst value for money
            worst_idx = max(selected_indices, 
                          key=lambda x: self.players[x]["Cost"] / self.players[x]["Performance_Score"] if x < len(self.players) else float('inf'))
            selected_indices.remove(worst_idx)
            solution[worst_idx] = 0
        
        # Add players if we have budget and less than 11 players
        available_indices = [i for i, val in enumerate(solution) if val == 0 and i < len(self.players)]
        available_indices.sort(key=lambda x: self.players[x]["Performance_Score"] / self.players[x]["Cost"], reverse=True)
        
        current_cost = sum(self.players[i]["Cost"] for i in selected_indices if i < len(self.players))
        
        for idx in available_indices:
            if len(selected_indices) >= 11:
                break
            if current_cost + self.players[idx]["Cost"] <= self.budget:
                solution[idx] = 1
                selected_indices.append(idx)
                current_cost += self.players[idx]["Cost"]
        
        return solution
    
    def _is_valid_solution(self, solution: List[int]) -> bool:
        """Check if solution is valid"""
        selected_indices = [i for i, val in enumerate(solution) if val == 1 and i < len(self.players)]
        
        if len(selected_indices) == 0:
            return False
            
        total_cost = sum(self.players[i]["Cost"] for i in selected_indices)
        return total_cost <= self.budget
    
    def _greedy_selection(self) -> List[int]:
        """Fallback greedy selection method"""
        solution = [0] * len(self.players)
        sorted_players = [(i, p) for i, p in enumerate(self.players)]
        sorted_players.sort(key=lambda x: x[1]["Performance_Score"] / x[1]["Cost"], reverse=True)
        
        selected_count = 0
        current_cost = 0
        
        for i, player in sorted_players:
            if selected_count >= 11:
                break
            if current_cost + player["Cost"] <= self.budget:
                solution[i] = 1
                selected_count += 1
                current_cost += player["Cost"]
        
        return solution
    
    def _evaluate_fitness(self, solution: List[int]) -> float:
        selected_indices = [i for i, val in enumerate(solution) if val == 1 and i < len(self.players)]
        
        if not selected_indices:
            return 0
        
        total_cost = sum(self.players[i]["Cost"] for i in selected_indices)
        total_performance = sum(self.players[i]["Performance_Score"] for i in selected_indices)
        
        # Heavily penalize budget violations
        if total_cost > self.budget:
            return 0
        
        # Reward solutions closer to 11 players
        player_count_penalty = abs(len(selected_indices) - 11) * 10
        
        return total_performance - player_count_penalty
    
    def _spiral_behavior(self, tuna: List[int], best_solution: List[int]) -> List[int]:
        new_tuna = tuna.copy()
        for i in range(len(tuna)):
            if random.random() < 0.3 and i < len(best_solution):
                new_tuna[i] = best_solution[i]
        return new_tuna
    
    def _straight_behavior(self, tuna: List[int]) -> List[int]:
        new_tuna = tuna.copy()
        for i in range(len(tuna)):
            if random.random() < 0.2:
                new_tuna[i] = 1 - new_tuna[i]
        return new_tuna

class RemoraOptimization:
    def __init__(self, selected_players: List[Dict], budget: float):
        self.selected_players = selected_players
        self.budget = budget
        self.role_requirements = {
            "Top-order Batsman": (2, 3),
            "Middle-order Batsman": (1, 3),
            "Wicketkeeper": (1, 1),
            "All-Rounder": (1, 3),
            "Spinner": (1, 2),
            "Pacer": (2, 3)
        }
        
    def balance_team(self) -> List[Dict]:
        if not self.selected_players:
            return []
            
        current_cost = sum(player["Cost"] for player in self.selected_players)
        
        # If already within budget and has good balance, return as is
        if current_cost <= self.budget and len(self.selected_players) <= 11:
            return self.selected_players[:11]
        
        # Otherwise, create a new balanced team within budget
        return self._create_budget_balanced_team()
    
    def _create_budget_balanced_team(self) -> List[Dict]:
        """Create a balanced team within budget constraints"""
        all_available = ipl_players.copy()
        sco = SalpChainOptimization(all_available, self.budget)
        enhanced_players = sco.optimize_performance_scores()
        
        # Filter players that fit in budget
        affordable_players = [p for p in enhanced_players if p["Cost"] <= self.budget]
        
        balanced_team = []
        remaining_budget = self.budget
        
        # First, ensure we have essential roles
        essential_roles = ["Wicketkeeper", "All-Rounder", "Pacer", "Top-order Batsman"]
        
        for role in essential_roles:
            role_players = [p for p in affordable_players 
                          if p["Role"] == role and p["Cost"] <= remaining_budget
                          and p not in balanced_team]
            
            if role_players and len(balanced_team) < 11:
                # Select best value player for this role
                best_player = max(role_players, 
                                key=lambda x: x["Performance_Score"] / x["Cost"])
                balanced_team.append(best_player)
                remaining_budget -= best_player["Cost"]
        
        # Fill remaining spots with best available players within budget
        remaining_players = [p for p in affordable_players 
                           if p not in balanced_team and p["Cost"] <= remaining_budget]
        remaining_players.sort(key=lambda x: x["Performance_Score"] / x["Cost"], reverse=True)
        
        for player in remaining_players:
            if len(balanced_team) >= 11:
                break
            if player["Cost"] <= remaining_budget:
                balanced_team.append(player)
                remaining_budget -= player["Cost"]
        
        return balanced_team[:11]

def generate_team_data(target_team: str, budget: float) -> Dict:
    if target_team != "ALL":
        available_players = [p for p in ipl_players if p["Team"] == target_team]
    else:
        available_players = ipl_players.copy()
    
    # Add more budget variety by including lower-cost alternatives
    if len(available_players) < 20:  # If team-specific, add some budget players from other teams
        other_players = [p for p in ipl_players if p["Team"] != target_team]
        available_players.extend(random.sample(other_players, min(10, len(other_players))))
    
    sco = SalpChainOptimization(available_players, budget)
    enhanced_players = sco.optimize_performance_scores()
    
    tso = TunaSwarmOptimization(enhanced_players, budget)
    selected_players = tso.select_players()
    
    roa = RemoraOptimization(selected_players, budget)
    final_team = roa.balance_team()
    
    # Ensure we don't exceed budget (final safety check)
    final_team.sort(key=lambda x: x["Performance_Score"] / x["Cost"], reverse=True)
    budget_compliant_team = []
    current_cost = 0
    
    for player in final_team:
        if current_cost + player["Cost"] <= budget and len(budget_compliant_team) < 11:
            budget_compliant_team.append(player)
            current_cost += player["Cost"]
    
    # If still not enough players, try to fill with cheapest available
    if len(budget_compliant_team) < 11:
        remaining_players = [p for p in enhanced_players if p not in budget_compliant_team]
        remaining_players.sort(key=lambda x: x["Cost"])
        
        for player in remaining_players:
            if len(budget_compliant_team) >= 11:
                break
            if current_cost + player["Cost"] <= budget:
                budget_compliant_team.append(player)
                current_cost += player["Cost"]
    
    final_team = budget_compliant_team
    
    total_cost = sum(player["Cost"] for player in final_team)
    total_performance = sum(player["Performance_Score"] for player in final_team)
    
    role_distribution = {}
    for player in final_team:
        role = player["Role"]
        role_distribution[role] = role_distribution.get(role, 0) + 1
    
    return {
        "team": final_team,
        "total_cost": round(total_cost, 2),
        "total_performance": round(total_performance, 2),
        "role_distribution": role_distribution,
        "target_team": target_team,
        "budget": budget,
        "budget_utilized": round((total_cost / budget) * 100, 1)
    }

def create_html_files():
    with open("index.html", "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IPL Team Generator 2025</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div id="particles-background"></div>
        
        <div class="header">
            <h1 class="main-title">IPL Team Generator</h1>
            <p class="subtitle">AI-Powered Bio-Inspired Team Selection System</p>
        </div>
        
        <div class="algorithm-card">
            <h3>🧠 Powered by Advanced AI Algorithms</h3>
            <div class="algorithm-list">
                <div class="algorithm-item">
                    <span class="algorithm-name">Salp Chain Optimization</span>
                    <span class="algorithm-desc">Performance Enhancement</span>
                </div>
                <div class="algorithm-item">
                    <span class="algorithm-name">Tuna Swarm Optimization</span>
                    <span class="algorithm-desc">Budget-Aware Selection</span>
                </div>
                <div class="algorithm-item">
                    <span class="algorithm-name">Remora Optimization</span>
                    <span class="algorithm-desc">Role Balance</span>
                </div>
            </div>
        </div>
        
        <form class="team-form" id="teamForm">
            <div class="form-group">
                <label for="team">Select IPL Team:</label>
                <select id="team" name="team" required>
                    <option value="ALL">All Teams (Mixed Squad)</option>
                    <option value="CSK">Chennai Super Kings (CSK)</option>
                    <option value="MI">Mumbai Indians (MI)</option>
                    <option value="RCB">Royal Challengers Bengaluru (RCB)</option>
                    <option value="RR">Rajasthan Royals (RR)</option>
                    <option value="LSG">Lucknow Super Giants (LSG)</option>
                    <option value="SRH">Sunrisers Hyderabad (SRH)</option>
                    <option value="PBKS">Punjab Kings (PBKS)</option>
                    <option value="KKR">Kolkata Knight Riders (KKR)</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="budget">Total Budget:</label>
                <div class="budget-container">
                    <input type="range" id="budget" name="budget" min="50" max="150" value="90" step="5">
                    <div class="budget-display">₹<span id="budgetValue">90</span> Crores</div>
                </div>
            </div>
            
            <button type="submit" class="generate-btn">
                <span class="btn-text">Generate Best Team</span>
                <div class="btn-loader"></div>
            </button>
        </form>
        
        <div class="loading-overlay" id="loadingOverlay">
            <div class="loading-content">
                <div class="spinner"></div>
                <h3>Generating Your Perfect Team</h3>
                <div class="loading-steps" id="loadingSteps">
                    <div class="step">🔄 Applying Salp Chain Optimization...</div>
                </div>
            </div>
        </div>
        
        <div id="results" class="results-section"></div>
    </div>
    
    <script src="script.js"></script>
</body>
</html>""")

def main():
    create_html_files()
    
    # Test with different budgets
    print("Testing budget constraints:")
    print("\n=== 50 Crore Budget Test ===")
    result_50 = generate_team_data("ALL", 50.0)
    print(f"Budget: ₹{result_50['budget']} Cr")
    print(f"Total Cost: ₹{result_50['total_cost']} Cr")
    print(f"Budget Utilized: {result_50['budget_utilized']}%")
    print(f"Players Selected: {len(result_50['team'])}")
    
    print("\n=== 100 Crore Budget Test ===")
    result_100 = generate_team_data("ALL", 100.0)
    print(f"Budget: ₹{result_100['budget']} Cr")
    print(f"Total Cost: ₹{result_100['total_cost']} Cr")
    print(f"Budget Utilized: {result_100['budget_utilized']}%")
    print(f"Players Selected: {len(result_100['team'])}")
    
    webbrowser.open("index.html")

if __name__ == "__main__":
    main()
