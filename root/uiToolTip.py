######################################
			#date: 27.01.2024
			#author: Kodo
######################################

		def ItemGetRace(self, item_vnum=0):
			male_races = [0, 5, 2, 7]
			female_races = [4, 1, 6, 3]
			anti_flags = ['WARRIOR', 'ASSASSIN', 'SURA', 'SHAMAN']
			# # You can extend lists of 'WOLFMAN':
			if app.ENABLE_WOLFMAN:
				male_races.append(8)
				anti_flags.append('WOLFMAN')

			item.SelectItem(item_vnum)

			# Create copies of lists of male and female races
			race_m = male_races[:]
			race_f = female_races[:]
			
			# Remove races that are marked as anti-race on the item
			for i, flag in enumerate(anti_flags):
				if item.IsAntiFlag(getattr(item, "ITEM_ANTIFLAG_" + flag)):
					if i < len(male_races) and male_races[i] in race_m:
						race_m.remove(male_races[i])
					if i < len(female_races) and female_races[i] in race_f:
						race_f.remove(female_races[i])

			# Remove male or female races if the item is marked as anti-race for gender
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
				race_f = [r for r in race_f if r not in female_races]
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
				race_m = [r for r in race_m if r not in male_races]

			# Get the player's race & Check if the player's race is available
			player_race = player.GetRace()
			if player_race in race_m or player_race in race_f:
				return player_race

			# Choose a random male race if no female races are available
			if not race_f and race_m:
				return self.__ChooseRaceFromList(race_m)

			# Choose a random female race if no male races are available
			if not race_m and race_f:
				return self.__ChooseRaceFromList(race_f)

			# Choose a random race from available male and female races
			if race_m and race_f:
				combined_races = race_f + race_m
				return self.__ChooseRaceFromList(combined_races)
				
			 # Return the player's race if no other races are available
			return player_race

		def __ChooseRaceFromList(self, race_list):
			if len(race_list) > 1:
				return race_list[app.GetRandom(0, len(race_list) - 1)]
			return race_list[0]
			

################################### USAGE ####################################

		## 1 ##	adapt in this class: ->>	class ItemToolTip(ToolTip):